from django.urls import path

from . import views

urlpatterns = [
    path(
        'orga/event/<slug:event>/p/samaware/',
        views.Dashboard.as_view(),
        name='dashboard'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/talks/<code>',
        views.TalkOverview.as_view(),
        name='talk_overview'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/missing-speakers/',
        views.MissingSpeakersList.as_view(),
        name='missing_speakers'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/no-recording/',
        views.NoRecordingList.as_view(),
        name='no_recording'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/tech-riders/',
        views.TechRiderList.as_view(),
        name='tech_rider_list'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/tech-riders/new',
        views.TechRiderEdit.as_view(),
        name='tech_rider_create'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/tech-riders/<int:pk>',
        views.TechRiderEdit.as_view(),
        name='tech_rider_update'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/tech-riders/<int:pk>/delete',
        views.TechRiderDelete.as_view(),
        name='tech_rider_delete'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/care-messages/',
        views.CareMessageList.as_view(),
        name='care_message_list'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/care-messages/new',
        views.CareMessageEdit.as_view(),
        name='care_message_create'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/care-messages/<int:pk>',
        views.CareMessageEdit.as_view(),
        name='care_message_update'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/care-messages/<int:pk>/delete',
        views.CareMessageDelete.as_view(),
        name='care_message_delete'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/fragments/search',
        views.SearchFragment.as_view(),
        name='search_fragment'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/fragments/internal-notes/<code>',
        views.InternalNotesFragment.as_view(),
        name='internal_notes_fragment'
    ),
    path(
        'orga/event/<slug:event>/p/samaware/fragments/tech-rider/<code>',
        views.TechRiderFragment.as_view(),
        name='tech_rider_fragment'
    )
]
