from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)


app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='home_page'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('about/', views.about, name='about_page'),

    path('search/', views.search, name='search'),

    path('soobin/', views.soobin, name='soobin'),
    path('yeongjun/', views.yeongjun, name='yeongjun'),
    path('huening_kai/', views.huening_kai, name='huening_kai'),
    path('taehyun/', views.taehyun, name='taehyun'),
    path('beomgyu/', views.beomgyu, name='beomgyu'),
]