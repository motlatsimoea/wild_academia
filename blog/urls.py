from django.urls import path
from .views import(
    CommentDeleteView, home, create_post, PostDeleteView,
     PostUpdateView, post_detail, tags, CommentDeleteView
)


urlpatterns = [
    path('', home, name='questions'),
    path('question/new/', create_post, name='create_post'),
    path('question/<uuid:pk>', post_detail, name='post-detail'),
    path('tag/<slug:tag_slug>', tags, name='tags'),
    path('question/<uuid:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('question/<uuid:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),
       
]