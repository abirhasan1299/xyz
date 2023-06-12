from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('kobita.urls')),
    path('',home,name="Home"),
    path('post/<str:slug>/',view_page,name="Post"),
    path('profile/<str:name>/',UserProfile,name="Profile"),
    path('all-post/',all_post,name="all_post"),
    path("users/",Users,name="users"),
    path("about/",About,name="about"),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
