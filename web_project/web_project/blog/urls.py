from django.urls import path

from web_project.blog.views import StartingPageView, AllPostsView, SinglePostView, ReadLaterView, add_post

urlpatterns = (
    path('', StartingPageView.as_view(), name='starting-page'),
    path('add-post/', add_post, name='add-post'),
    path('posts/', AllPostsView.as_view(), name='posts-page'),
    path('path/<slug:slug>/', SinglePostView.as_view(), name='post-detail-page'),
    path('read-later/', ReadLaterView.as_view(), name='read-later')
)