from django.urls import path
from . import views
urlpatterns = [

    path('areas', views.areas , name="Homepage Rendering"),
    path('areas/<int:pk>', views.bookarea , name="Homepage Rendering"),
    path('cheakout/<int:pk>', views.cheakout , name="Homepage Rendering"),
    path('cheakout', views.cheakout_list , name="Homepage Rendering"),

]
