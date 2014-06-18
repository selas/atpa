# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render_to_response, render, redirect
from django.views.decorators.csrf import csrf_protect
from django.db.models import Max
from django.utils import timezone
from appli.models import Question, Reponse, Question_ligne, Reponse_ligne, Type
from appli.forms import Connexion, AjoutQuestion#, AfficheQuestion
from datetime import datetime, timedelta
import socket
import time
import logging

logger = logging.getLogger(__name__)


@csrf_protect
def connexion(request):
	if request.method == 'POST': # If the form has been submitted...
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		#form = Connexion(request.POST) # A form bound to the POST data

		if user is not None:
			if user.is_active:
				login(request, user)
				# Redirect to a success page.
				return redirect("accueil") 

			else:
				# Return a 'disabled account' error message
				return redirect(".")

		else:
			# Return an 'invalid login' error message.
			return redirect('.')

	else:
		# Un formulaire vide
		form = Connexion() 
		#On recupere le group ayant pour nom enseignant
		group = Group.objects.filter(name='enseignant' ) 
		#On recupere les utilisateurs ayant pour group celui precedemment recupere
		users = User.objects.filter(groups=group )

		return render(request, 'appli/connexion.html', {
			'form': form,
			'users': users,
			})


def accueil(request):

	if request.user.is_authenticated():

			question_list = Question.objects.filter(enseignant=request.user)
			return render(request, 'appli/accueil.html' , { 'question_list' : question_list })

	else:
		return redirect(reverse('connexion'))


def deconnexion(request):

	logout(request)
	return redirect('connexion')


def affichageQuestion(request, question_id=None):

	if question_id:

		maQuestion = Question.objects.get(pk=question_id)
		
		question = maQuestion.libelle
		
		temps = maQuestion.temps
		
		maReponse = Reponse.objects.filter(question=maQuestion)
		
		question_list = Question.objects.filter(enseignant=request.user)

		return render(request, 'appli/accueil.html', { 
			'question_id': question_id, 'question': question, 'temps': temps,
		 	'maReponse': maReponse, 'question_list' : question_list
			})
		
	else:

		question = 'pas question'
		temps = 'pas temps'
		maReponse = 'pas reponse'
		question_list = Question.objects.filter(enseignant=request.user)


		return render(request, 'appli/accueil.html', {
			'question': question, 'temps': temps, 'maReponse': maReponse, 'question_list' : question_list
			})


def new_question(request):
	if request.method == 'POST' :

		# QUESTION
		libelle = request.POST['intituleQuestion']
		enseignant = request.user
		temps = request.POST['temps']
		typeQuestion = request.POST['type_question']
		monObjetType = Type.objects.get(pk=typeQuestion)

		maQuestion = Question(enseignant = enseignant , libelle = libelle , temps = temps , typeQuestion = monObjetType)
		maQuestion.save()

		# REPONSES
		listeReponses_lib = request.POST['champReponses_lib']
		listeReponses_bool = request.POST['champReponses_bool']
		logger.error(listeReponses_lib)
		idQuestion = maQuestion.id
		monObjetQuestion = Question.objects.get(pk=idQuestion)

		champReponsesSplit_lib = listeReponses_lib.split('|')
		champReponsesSplit_bool = listeReponses_bool.split('|')

		logger.error(len(champReponsesSplit_lib))

		logger.error(champReponsesSplit_lib)
		logger.error(champReponsesSplit_bool)

		for i in range(0,len(champReponsesSplit_lib)):
			logger.error(champReponsesSplit_lib[i])
			logger.error(champReponsesSplit_bool[i])

			if champReponsesSplit_bool[i] == 'true' :
				champReponsesSplit_bool[i] = True
			else :
				champReponsesSplit_bool[i] = False

			maReponse = Reponse(question = monObjetQuestion, libelle = champReponsesSplit_lib[i] , reponseValide = champReponsesSplit_bool[i])
			maReponse.save()

		# Redirect to a success page.
		question_list = Question.objects.filter(enseignant=request.user)
		return render(request, 'appli/accueil.html' , {'question_list' : question_list, 'enseignant' : enseignant , 'libelle' : libelle , 'temps' : temps , 'typeReponse' :'Choix simple' })

	else:
		types = Type.objects.all()
		form = AjoutQuestion() # An unbound form
		return render(request, 'appli/formQuestion.html', {
			'form': form, 'types':types,
			})


#def choixquestion_view(request):
#	if request.method=='POST':
#		form = ChoixQuestion(request.POST)
#		if form.is_valid:
#			question = form.cleaned_data.get('question')
#			#fecrire du code pour savoir ce que l on va faire
#	else:
#		form = ChoixQuestion
#	return render(request,'appli/ajout.html',
#			{'form':form})
#			#context_instance = RequestContext(request) )


#acces a la page pour repondre a une question pour une personne identifiée
def question_posee(request, question_posee_id=None, enseignant_id=None):
	if request.user.is_authenticated():
		if request.method == 'POST' :
			
			question = Question.objects.get(pk=question_posee_id)

			question_ligne = Question_ligne(question=question, dureeActivite=question.temps)
			question_ligne.save()

			reponses = Reponse.objects.filter(question=question_ligne.question)

			return render(request, 'appli/enseignant_question.html', { 
				'question_ligne':question_ligne,
			 	'reponses':reponses 
			 	})

		return redirect("accueil")
	else:
		if enseignant_id :

			#recupere les question d'un enseignant
			question = Question.objects.filter(enseignant=enseignant_id)
			#recupere toute les question posée par l'enseignant
			question_ligne = Question_ligne.objects.filter(question=question)
			# recupere la date maximale de mise en ligne
			qu = question_ligne.aggregate(dateDebut = Max('dateDebut'))
			# question_active = Question_ligne.objects.get(dateDebut=question)

			if qu["dateDebut"] :
				question_ligne = Question_ligne.objects.get(dateDebut=qu["dateDebut"])

				dateFinished = question_ligne.dateDebut + timedelta(seconds=question_ligne.dureeActivite)
				
				naive = datetime.utcnow()
				aware = naive.replace(tzinfo=timezone.utc)

				if aware < dateFinished:

					reponses = Reponse.objects.filter(question=question_ligne.question)
					return render(request, 'appli/enseignant_question.html', { 
						'question_ligne':question_ligne,
					 	'reponses':reponses
					 	 })
			
		return render(request, 'appli/enseignant_question.html', {})



def reponse(request, question_ligne_id):
	if request.method == 'POST' :

		idQuestion = request.POST['question']
		question = Question.objects.get(pk=idQuestion)
		ip = IP()

		#recupere la question en ligne correspondant 
		question_ligne = Question_ligne.objects.get(pk=question_ligne_id)

		dateFinished = question_ligne.dateDebut + timedelta(seconds=question_ligne.dureeActivite)
		
		naive = datetime.utcnow()
		aware = naive.replace(tzinfo=timezone.utc)

		if aware < dateFinished:

			#Recupere le nombre d'enregistrement present dans la bdd 
			#en fonction de l'utilisateur et de la question mise en ligne
			reponse_ligne = Reponse_ligne.objects.filter(question=question_ligne, ip=ip).count()

			if reponse_ligne < 1:
				for item in request.POST:
					if (item != "csrfmiddlewaretoken") and (item != "question"):
						idReponse = request.POST[item]
						reponses = Reponse.objects.filter(question=question_ligne.question)
						reponse_ligne = Reponse_ligne(question=question_ligne, reponse=idReponse, ip=ip)
						reponse_ligne.save()
			else : 
				error = "true"
				return render(request, 'appli/enseignant_question.html', {'error':error})

	return redirect("accueil") 


def IP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    return s.getsockname()[0]

# return HttpResponse(str(idReponse))
