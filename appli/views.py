# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, render, redirect
from appli.models import Question, Reponse, Question_ligne, Type
from appli.forms import Connexion, AjoutQuestion#, AfficheQuestion
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

#from django.contrib.auth.models import User


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
		#Lorsque l'on click sur deconnexion, aucune methode post n'est passé
		#Donc ensuite, on test si il existe un utilisateur ou non 
		#Si un utilise existe, on le deconnecte 
		#Puis on renvoi sur la page de connection

		form = Connexion() # An unbound form
		return render(request, 'appli/connexion.html', {
			'form': form,
			})


def accueil(request):

	if request.user.is_authenticated():

			question_list = Question.objects.filter(enseignant=request.user)
			return render(request, 'appli/accueil.html' , { 'question_list' : question_list })

	else:
		return redirect('connexion')


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
		listeReponses = request.POST['champReponses']
		logger.error(listeReponses)
		idQuestion = maQuestion.id
		monObjetQuestion = Question.objects.get(pk=idQuestion)

		champReponsesSplit = listeReponses.split('|')
		logger.error(champReponsesSplit)
		logger.error(len(champReponsesSplit))
		for i in range(0,len(champReponsesSplit)):
			logger.error(champReponsesSplit[i])
			maReponse = Reponse(question = monObjetQuestion, libelle = champReponsesSplit[i] , reponseValide = True)
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



def question_posee(request, question_posee_id):
	if request.method == 'POST' : 
		
		maQuestion = Question.objects.get(pk=question_posee_id)
		maQuestion_posee = Question_ligne(question=maQuestion, dureeActivite=maQuestion.temps)
		maQuestion_posee.save()
		return redirect("question_en_ligne")


def question_en_ligne(request):
	#if request.method == 'POST' : 

	if request.user.is_authenticated():

		connecte = request.user
		return render(request, 'appli/enseignant_question.html', {'connecte':connecte})

	else:
		connecte = None
		question_posee = None # A modifier la prochaine fois
		return render(request, 'appli/enseignant_question.html', {'connecte':connecte, 'question_posee':question_posee})

		


		
		
	
