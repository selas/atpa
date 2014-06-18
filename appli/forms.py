# -*- coding: utf-8 -*-
from django import forms
from appli.models import Type
from datetime import date

class Connexion(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Login', 'class':'input-small'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'input-small'}))

class AjoutQuestion(forms.Form):
	mesTypes = Type.objects.all()
	CHOICES = []
	for monType in mesTypes :
		CHOICES.append([monType.id, monType.libelle])

	intituleQuestion = forms.CharField(widget = forms.Textarea(attrs = {'rows' : '2' ,'class':'special'}))
	
	temps = forms.TimeField(label="Temps pour répondre", required=True, input_formats=("%M:%S",))

	typeQuestion = forms.ChoiceField(widget=forms.Select(attrs = {'class':'form-control input-sm'}), choices=CHOICES)

	intituleReponseBonne1 = forms.CharField(max_length = 100)
	intituleReponseMauvaise1 = forms.CharField(max_length = 100)