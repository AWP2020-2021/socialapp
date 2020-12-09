from django.urls import path
from app.views import (
  index, PostListView, post_detail,
  PostDetail, UserProfileView,
)

urlpatterns = [
  path('', index, name='post_list'),
  path('', PostListView.as_view(), name='post_list'),
  path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
  path('userprofile', UserProfileView.as_view(), name='user_profile'),
]