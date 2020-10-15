from django.shortcuts import render, redirect 
import requests
from django.http import HttpResponse
from .models import *
from .forms import *



# Create your views here.
def index(request):


	# API from openweather
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
	
	cities = Weather.objects.all()

	city_data = []

	for city in cities:
		api = SecureData.objects.get(id=1)
		raw = (requests.get(url.format(city,api.api_key))).json()

		weather_data = {
			'city': city,
			'temperature': raw['main']['temp'],
			'description': raw['weather'][0]['description'],
			'icon': raw['weather'][0]['icon'],

		}

	city_data.append(weather_data)

	# Note Taking App 

	note = Note.objects.all()

	form = NoteForm()

	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')	

	else:	
		context = {'note': note, 'form': form, 'weather_data': weather_data}
		return render(request, 'index.html', context)


def updateNote(request, pk):
	notee = Note.objects.get(id=pk)

	form = NoteForm(instance=notee)

	if request.method == 'POST':
		form = NoteForm(request.POST, instance=notee)
		if form.is_valid():
			form.save()
		return redirect('/')	

	context = {'form':form}

	return render(request, 'update_note.html', context )


def deleteNote(request, pk):
	item = Note.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()

		return redirect('/')
		
	context = {'item' : item}
	return render(request, 'delete_note.html', context )

def weatherView(request):

	

	return render(request, '/', context)
	

	


