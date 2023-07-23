from django.urls import path

from web_project.blog.views import starting_page, posts, post_detail

urlpatterns = (
    path('', starting_page, name='starting-page'),
    path('posts/', posts, name='posts-page'),
    path('path/<slug:slug>/', post_detail, name='post-detail-page'),
)