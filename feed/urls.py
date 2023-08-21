from django.urls import path
from .views import post, create_feed, feed_details, FeedDeleteView, stream, OpinionDeleteView, ReplyDeleteView

urlpatterns = [
    path('', post, name='posts'),
    path('new/', create_feed, name='create_feed'),
    path('<uuid:pk>', feed_details, name='feed-detail'),
    path('<uuid:pk>/delete', FeedDeleteView.as_view(), name='feed-delete'),
    path('reply/<int:pk>/delete/', OpinionDeleteView.as_view(), name='opinion-delete'),
    path('opinion/<int:pk>/delete/', ReplyDeleteView.as_view(), name='reply-delete'),
    path('stream/', stream, name='feed-stream'),

]