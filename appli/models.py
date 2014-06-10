# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from datetime import datetime 
from django.db import models


TYPEREP_CHOICES = (
	('Choix double', 'Choix double'),
	('Choix multiple', 'Choix multiple'),
	('Saisie', 'Saisie')
)


class Question(models.Model):
	enseignant = models.ForeignKey(User)
	libelle = models.CharField("Votre question" , max_length = 250)
	temps = models.IntegerField("Temps pour répondre" , max_length = 4)
	typeReponse = models.CharField("Type de question", max_length=20, choices=TYPEREP_CHOICES)

	def __unicode__(self):
		return self.libelle
		

class Reponse(models.Model):
	question = models.ForeignKey(Question)
	libelle = models.CharField( "Votre réponse" , max_length = 100)
	reponseValide = models.BooleanField("Cette réponse est-elle bonne ou non", default=True)

	def __unicode__(self):
		return self.libelle


class Question_ligne(models.Model):
	question = models.ForeignKey(Question)
	dateDebut = models.DateTimeField("Date de dépôt de la question", default=datetime.now, blank=True)
	dureeActivite = models.IntegerField("Temps pour répondre", max_length = 4)

	def __unicode__(self):
		return self.question


class Reponse_ligne(models.Model):
	question = models.ForeignKey(Question_ligne)
	reponse = models.CharField("La reponse saisie", max_length = 100)
	ip = models.CharField("L'adresse IP'", max_length = 39)

	def __unicode__(self):
		return self.question

