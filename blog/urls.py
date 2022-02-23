"""URL Paths for the website blog"""
from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # when i remove the hastag above the blog works but the admin add post does not?
    path('<int:post_id>/', views.PostDetail, name='postdetail'),
    path('add_post/', views.add_post, name='add_post'),
]
