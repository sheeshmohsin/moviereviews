from django import forms
from app.models import Movie, Review

class MovieForm(forms.ModelForm):

	class Meta:
		model = Movie
		fields = ("name", "description", "poster")
		widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Movie Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Movie Description'}),
        }