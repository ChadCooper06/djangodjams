from django.urls import path

from . import views, individual_song

urlpatterns = [
    path('', views.index, name='index'),
    path("api/json/<int:id>", individual_song)
]