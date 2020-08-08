from django.urls import path

from blog.api.views import (
    api_blog_detail_view,
    api_blog_create_view,
    api_blog_delete_view,
    api_blog_update_view,
)

app_name = 'blog'
urlpatterns = [
    path('<slug>/',api_blog_detail_view,name="detail"),
    path('<slug>/update',api_blog_update_view,name="update"),
    path('create',api_blog_create_view,name="create"),
    path('<slug>/delete',api_blog_delete_view,name="delete"),
]


