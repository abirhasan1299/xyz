from django.urls import path
from .views import *

urlpatterns = [
    #path("<uuid:ud>/",kobita_home,name="kobita"),
    path("signup/",signup,name="signup"),
    path('login/',Login,name="Login"),
    path('logout/',Logout,name="logout"),
]
