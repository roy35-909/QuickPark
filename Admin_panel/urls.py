from django.urls import path
from . import views
urlpatterns = [

    path('', views.dashboard , name="Dashboard Rendering"),
    path('area', views.dashboard_area , name="Dashboard Area Rendering"),
    path('delete_area/<int:pk>', views.delete_area , name="Delete Area"),
    path('slots', views.dashboard_slots , name="Slots"),
    path('slots_action/<int:pk>/<str:action>', views.dashboard_slot_action , name="Slots"),
    path('regiser_staff', views.dashboard_regiser_staff , name="Slots"),
    path('view_payment', views.dashboard_payment , name="Payment"),
    path('delete_staff/<int:pk>', views.delete_staff , name="Slots"),


]
