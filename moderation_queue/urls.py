from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import (
    upload_photo, PhotoUploadSuccess, PhotoReviewList, PhotoReview,
    SuggestLockView, SuggestLockReviewListView
)

urlpatterns = patterns('',
    url(r'^photo/upload/(?P<person_id>\d+)$',
        upload_photo,
        name="photo-upload"),
    url(r'^photo/review$',
        PhotoReviewList.as_view(),
        name="photo-review-list"),
    url(r'^photo/review/(?P<queued_image_id>\d+)$',
        PhotoReview.as_view(),
        name="photo-review"),
    url(r'^photo/upload/(?P<person_id>\d+)/success$',
        PhotoUploadSuccess.as_view(),
        name="photo-upload-success"),
    url(r'^suggest-lock/(?P<election_id>.*)/$',
        SuggestLockView.as_view(),
        name="constituency-suggest-lock"),
    url(r'^suggest-lock/$',
        SuggestLockReviewListView.as_view(),
        name="suggestions-to-lock-review-list"),
)
