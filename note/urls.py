from django.urls import path
from . import views

urlpatterns = [
	path('', views.index , name="index"),
	path('weather.html',views.weatherView, name="weather_view"),
	path('update_note/<str:pk>/', views.updateNote, name="update_note"),
	path('delete_note/<str:pk>/', views.deleteNote, name="delete_note"),
]