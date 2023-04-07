from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from account import views as account_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),

    path('register/', account_views.register, name='register'),
    path('profile/', account_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

