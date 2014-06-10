# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, render, redirect
from appli.models import Question, Reponse, Question_ligne
from appli.forms import Connexion, AjoutQuestion#, AfficheQuestion
from django.views.decorators.csrf import csrf_protect
from datetime import datetime 

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
	if request.method == 'POST' : # If the form has been submitted...
		libelle = request.POST['intituleQuestion']
		username = request.user
		
		temps = request.POST['temps'] # A form bound to the POST data
#		typeReponse = request.POST['typeReponse']

		# form = AjoutQuestion(request.POST)
		maQuestion=Question(enseignant = username , libelle = libelle , temps = temps , typeReponse = 'Choix simple')
		maQuestion.save()
		idQuestion = maQuestion.id
		monObjetQuestion = Question.objects.get(pk=idQuestion)
		
		intituleReponseBonne1 = request.POST['intituleReponseBonne1']
		# intituleReponseBonne2 = request.POST['intituleReponseBonne2']
		# intituleReponseBonne3 = request.POST['intituleReponseBonne3']
		# intituleReponseBonne4 = request.POST['intituleReponseBonne4']
		intituleReponseMauvaise1 = request.POST['intituleReponseMauvaise1']
		# intituleReponseMauvaise2 = request.POST['intituleReponseMauvaise2']
		# intituleReponseMauvaise3 = request.POST['intituleReponseMauvaise3']
		# intituleReponseMauvaise4 = request.POST['intituleReponseMauvaise4']
		maQuestionReponse1 = Question_reponse(question = monObjetQuestion, libelle = intituleReponseBonne1 , reponseValide = True)
		# maQuestionReponse1.save()
		# maQuestionReponse2 = Question_reponse(question_r = maQuestion.id , libelle_r = intituleReponseBonne2 , reponseValide_r = 'Choix simple')
		# maQuestionReponse3 = Question_reponse(question_r = maQuestion.id , libelle_r = intituleReponseBonne3 , reponseValide_r = 'Choix simple')
		# maQuestionReponse4 = Question_reponse(question_r = maQuestion.id , libelle_r = intituleReponseBonne4 , reponseValide_r = 'Choix simple')

		maQuestionReponse5 = Question_reponse(question = monObjetQuestion , libelle = intituleReponseMauvaise1 , reponseValide = False)
		# maQuestionReponse6 = Question_reponse(question_r = maQuestion.id , libelle_r = intituleReponseMauvaise2 , reponseValide_r = 'Choix simple')
		# maQuestionReponse7 = Question_reponse(question_r = maQuestion.id , libelle_r = intituleReponseMauvaise3 , reponseValide_r = 'Choix simple')
		# maQuestionReponse8 = Question_reponse(question_r = maQuestion.id , libelle_r = intituleReponseMauvaise4 , reponseValide_r = 'Choix simple')
		
		maQuestionReponse1.save()
		maQuestionReponse5.save()
			# Redirect to a success page.
		question_list = Question.objects.filter(enseignant=request.user)
		return render(request, 'appli/accueil.html' , {'question_list' : question_list, 'enseignant' : username , 'libelle' : libelle , 'temps' : temps , 'typeReponse' :'Choix simple' })
		
	else:
		form = AjoutQuestion() # An unbound form
		return render(request, 'appli/formQuestion.html', {
			'form': form, 
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

		


		
		
	
