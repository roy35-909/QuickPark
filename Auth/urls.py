from django.urls import path
from . import views
urlpatterns = [

    path('login', views.login , name="Homepage Rendering"),
    path('register', views.register , name="Homepage Rendering"),
    path('logout',views.logout,name="Logout")
]
