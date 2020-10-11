from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *



# Create your views here.
def index(request):
	note = Note.objects.all()

	form = NoteForm()

	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')	

	else:	
		context = {'note': note, 'form': form}
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