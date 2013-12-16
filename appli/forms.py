# -*- coding: utf-8 -*-
from django import forms

class Connexion(forms.Form):
	
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Login', 'class':'input-small'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'input-small'}))
	

class AjoutQuestion(forms.Form):

	TYPEREP_CHOICES = (
		('Choix simple', 'Choix simple'),
		('Choix multiple', 'Choix multiple'),
		('Choix alphanumerique', 'Choix alphanumerique')
	)

	intituleQuestion = forms.CharField(max_length=100)
	temps = forms.IntegerField()
	typeReponse = forms.MultipleChoiceField(widget=forms.Select, choices=TYPEREP_CHOICES)

	intituleReponse = forms.CharField(max_length = 100)
	reponseValide_oui = forms.BooleanField()
	reponseValide_non = forms.BooleanField()

	#intituleReponse_non = forms.CharField(max_length = 100)
	#reponseValide_non = forms.BooleanField(default=True)