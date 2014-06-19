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

	HEURE = []
	for i in range(0,24) :
		HEURE.append([i,i])

	MINSEC = []
	for i in range(0,60) :
		MINSEC.append([i,i])

	intituleQuestion = forms.CharField(widget = forms.Textarea(attrs = {'rows' : '3', 'style' : 'resize:vertical', 'class' : 'form-control'}))
	
	temps = forms.TimeField(widget=forms.TimeInput(format='%H:%M:%S', attrs = {'class':'form-control input-sm', 'type':'hidden'}), label="Temps pour répondre", required=True)

	typeQuestion = forms.ChoiceField(widget=forms.Select(attrs = {'class':'form-control input-sm'}), choices=CHOICES)

	listeHeure = forms.ChoiceField(widget=forms.Select(attrs = {'class':'input-sm'}), choices=HEURE)
	listeMinute = forms.ChoiceField(widget=forms.Select(attrs = {'class':'input-sm'}), choices=MINSEC)
	listeSeconde = forms.ChoiceField(widget=forms.Select(attrs = {'class':'input-sm'}), choices=MINSEC)

	intituleReponseBonne1 = forms.CharField(max_length = 100)
	intituleReponseMauvaise1 = forms.CharField(max_length = 100)