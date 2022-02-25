"""URL Paths for the website blog"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('addpost/', views.add_post, name='addpost'),
    path('<int:post_id>/', views.PostDetail, name='postdetail'),
    path('editpost/<int:post_id>/', views.edit_post, name='editpost'),
    path('deletepost/<int:post_id>/', views.delete_post, name='deletepost'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]
