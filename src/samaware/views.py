import datetime

from django.utils import timezone
from django.views.generic import ListView, TemplateView
from django_context_decorator import context
from pretalx.common.views.mixins import EventPermissionRequired, Sortable

import samaware

from . import forms, queries


class Dashboard(EventPermissionRequired, TemplateView):

    permission_required = samaware.REQUIRED_PERMISSIONS
    template_name = 'samaware/dashboard.html'
    timeframe = datetime.timedelta(hours=4)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['total_speakers'] = queries.get_all_speakers(self.request.event)
        data['arrived_speakers'] = queries.get_arrived_speakers(self.request.event)
        data['unreleased_changes'] = self.request.event.wip_schedule.changes
        data['no_recording_sessions'] = queries.get_sessions_without_recording(self.request.event)

        data['sessions_missing_speakers'] = queries.get_sessions_missing_speakers(self.request.event,
                                                                                  self.timeframe)
        data['no_recording_sessions_4h'] = queries.get_sessions_without_recording(self.request.event,
                                                                                  self.timeframe)

        return data


class NoRecordingList(EventPermissionRequired, Sortable, ListView):

    permission_required = samaware.REQUIRED_PERMISSIONS
    sortable_fields = ('submission__track__name', 'submission__title', 'start', 'room')
    default_sort_field = 'start'
    template_name = 'samaware/no_recording_list.html'
    context_object_name = 'slots'
    upcoming_timeframe = datetime.timedelta(hours=4)

    @context
    def filter_form(self):
        return forms.NoRecordingFilter(self.request.GET)

    def get_queryset(self):
        submissions = queries.get_sessions_without_recording(self.request.event)
        slots = self.request.event.wip_schedule.talks.filter(submission__in=submissions)

        filter_form = self.filter_form()
        if filter_form.is_valid() and filter_form.cleaned_data.get('upcoming'):
            now = timezone.now()
            upcoming_threshold = now + self.upcoming_timeframe
            slots = slots.filter(start__gt=now, start__lt=upcoming_threshold)

        return self.sort_queryset(slots.select_related('submission', 'room'))
