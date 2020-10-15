from django import forms
from django.forms import ModelForm, TextInput

from .models import *

class NoteForm(forms.ModelForm):
	title = forms.CharField(widget= forms.Textarea(attrs={'placeholder':'Take your note'}))

	class Meta:
		model = Note
		fields = '__all__'
