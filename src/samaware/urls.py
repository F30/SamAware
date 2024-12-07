from django.urls import re_path
from pretalx.event.models.event import SLUG_REGEX

from . import views

urlpatterns = [
    re_path(
        rf'^orga/event/(?P<event>{SLUG_REGEX})/p/samaware/$',
        views.DashboardView.as_view(),
        name='dashboard'
    )
]