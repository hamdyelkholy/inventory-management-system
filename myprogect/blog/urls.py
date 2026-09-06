from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blogs/create/', views.create_blog, name='create_blog'),
    path('blogs/<int:id>/edit/', views.edit_blog, name='edit_blog'),
    path('blogs/<int:id>/delete/', views.delete_blog, name='delete_blog'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
]