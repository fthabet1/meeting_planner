from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name = "detail"),
    path('rooms', views.rooms, name = "rooms"),
    path('rooms/<int:id>', views.room_info, name = "room_info"),
    path('new', views.new, name = "new"),
]