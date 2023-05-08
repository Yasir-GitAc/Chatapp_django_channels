from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path("<str:room_name>/", views.room, name="room"),
  # path("chat/<str:chat_box_name>/", views.chat_box, name="chat"),
]
 