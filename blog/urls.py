from django.urls import path
from blog.views import (
    create_blog_view,
    detail_blog_view,
    edit_blog_view,
    like_post_view,
)

app_name = 'blog'

urlpatterns = [
    path('create',create_blog_view,name='create'),
    path('<slug>',detail_blog_view,name='detail'),
    path('<slug>/edit',edit_blog_view,name='edit'),
    path('<slug>/like',like_post_view,name='like'),
]