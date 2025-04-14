from django.urls import path

from posts.views import PostView

urlpatterns=[
  path(route="",view=PostView.as_view(),name="posts"),
]