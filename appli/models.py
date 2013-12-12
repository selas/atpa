# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from datetime import datetime 
from django.db import models


TYPEREP_CHOICES = (
	('Choix simple', 'Choix simple'),
	('Choix multiple', 'Choix multiple'),
	('Choix alphanumerique', 'Choix alphanumerique')
)


class Question(models.Model):
	enseignant_q = models.ForeignKey(User)
	libelle_q = models.CharField("Votre question" , max_length = 250)
	temps_q = models.IntegerField("Temps pour répondre" , max_length = 4)
	typeReponse_q = models.CharField("Type de question", max_length=20, choices=TYPEREP_CHOICES)

	def __unicode__(self):
		return self.libelle_q


class Question_reponse(models.Model):
	question_r = models.ForeignKey(Question)
	libelle_r = models.CharField( "Votre réponse" , max_length = 100)
	reponseValide_r = models.BooleanField("Cette réponse est-elle bonne ou non", default=True)

	def __unicode__(self):
		return self.libelle_r


class Question_posee(models.Model):
	question_qa = models.ForeignKey(Question)
	dateDebut_qa = models.DateTimeField("Date de dépos de la question", default=datetime.now, blank=True)
	dureeActivite_qa = models.IntegerField("Temps pour répondre", max_length = 4)

	def __unicode__(self):
		return self.question_qa


class Reponse_saisie(models.Model):
	question_s = models.ForeignKey(Question_posee)
	reponse_s = models.CharField("La reponse saisie", max_length = 100)
	ip_s = models.CharField("L'adresse IP'", max_length = 39)

	def __unicode__(self):
		return self.question_s

