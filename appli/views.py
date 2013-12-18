# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.shortcuts import render
from appli.models import Question, Question_reponse
from appli.forms import Connexion, AjoutQuestion
from django.contrib.auth.models import User



def connexion(request):
	if request.method == 'POST': # If the form has been submitted...
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		form = Connexion(request.POST) # A form bound to the POST data

		if user is not None:
			if user.is_active:
				login(request, user)
				form = Connexion() # An unbound form
				# Redirect to a success page.

				question_list_simple = Question.objects.filter(typeReponse_q="Choix simple",enseignant_q = user)
				question_list_multiple = Question.objects.filter(typeReponse_q="Choix multiple",enseignant_q = user)
				question_list_alphanumerique = Question.objects.filter(typeReponse_q="Choix alphanumerique",enseignant_q = user)
				return render(request, 'appli/accueil.html' , { 'question_list_simple' : question_list_simple, 'question_list_multiple' : question_list_multiple, 'question_list_alphanumerique' : question_list_alphanumerique })

			else:
				# Return a 'disabled account' error message
				error = "Compte desactivé"
				return render(request, 'appli/connexion.html', {
					'form': form,'error': error
					})
		else:
			# Return an 'invalid login' error message.
			error = "login ou mot de passe invalid"
			return render(request, 'appli/connexion.html', {
				'form': form,'error': error
				})
	else:

		if request.user is not None:

			logout(request)
			form = Connexion() # An unbound form
			return render(request, 'appli/connexion.html', {
				'form': form,
				})
			

		else:
			form = Connexion() # An unbound form
			return render(request, 'appli/connexion.html', {
				'form': form,
				})


		#if form.is_valid(): # All validation rules pass
			#Redirect to a success page.
		#	return HttpResponse("Connexion ok")
		#else:
			#Return a 'disabled account' error message 

def deconnexion(request):
	logout(request)
	form = Connexion() # An unbound form
	return render(request, 'appli/connexion.html', {
					'form': form
					})

def new_question(request):
	if request.method == 'POST' : # If the form has been submitted...
		libelle_q = request.POST['intituleQuestion']
		username_q = request.user
		
		temps_q = request.POST['temps'] # A form bound to the POST data
#		typeReponse_q = request.POST['typeReponse']

		# form = AjoutQuestion(request.POST)
		# if form.is_valid(): # All validation rules pass
		maQuestion=Question(enseignant_q = username_q , libelle_q = libelle_q , temps_q = temps_q , typeReponse_q = 'Choix simple')
		maQuestion.save()
		
		intituleReponseBonne1 = request.POST['intituleReponseBonne1']
		# intituleReponseBonne2 = request.POST['intituleReponseBonne2']
		# intituleReponseBonne3 = request.POST['intituleReponseBonne3']
		# intituleReponseBonne4 = request.POST['intituleReponseBonne4']
		intituleReponseMauvaise1 = request.POST['intituleReponseMauvaise1']
		# intituleReponseMauvaise2 = request.POST['intituleReponseMauvaise2']
		# intituleReponseMauvaise3 = request.POST['intituleReponseMauvaise3']
		# intituleReponseMauvaise4 = request.POST['intituleReponseMauvaise4']

		# maQuestionReponse1 = Question_reponse(question_r = 23, libelle_r = intituleReponseBonne1 , reponseValide_r = True)
		# maQuestionReponse1.save()
		# maQuestionReponse2 = Question_reponse(question_r = maQuestion.id , libelle_r = intituleReponseBonne2 , reponseValide_r = 'Choix simple')
		# maQuestionReponse3 = Question_reponse(question_r = maQuestion.id , libelle_r = intituleReponseBonne3 , reponseValide_r = 'Choix simple')
		# maQuestionReponse4 = Question_reponse(question_r = maQuestion.id , libelle_r = intituleReponseBonne4 , reponseValide_r = 'Choix simple')

	#	maQuestionReponse5 = Question_reponse(question_r = monId , libelle_r = intituleReponseMauvaise1 , reponseValide_r = False)
		# maQuestionReponse6 = Question_reponse(question_r = maQuestion.id , libelle_r = intituleReponseMauvaise2 , reponseValide_r = 'Choix simple')
		# maQuestionReponse7 = Question_reponse(question_r = maQuestion.id , libelle_r = intituleReponseMauvaise3 , reponseValide_r = 'Choix simple')
		# maQuestionReponse8 = Question_reponse(question_r = maQuestion.id , libelle_r = intituleReponseMauvaise4 , reponseValide_r = 'Choix simple')
		
		# maQuestionReponse1.save()
		# maQuestionReponse5.save()
			# Redirect to a success page.
		return render(request, 'appli/essai.html' , {'enseignant_q' : username_q , 'libelle_q' : libelle_q , 'temps_q' : temps_q , 'typeReponse_q' :'Choix simple' })
		# else:
			# Return a 'disabled account' error message
			# return render(request, 'appli/formQuestion.html', {'enseignant_q' : username , 'libelle_q' : libelle_q , 'temps_q' : temps , 'typeReponse_q' :'Choix simple' })
			
	else:
		form = AjoutQuestion() # An unbound form
		return render(request, 'appli/formQuestion.html', {
			'form': form, 
			})



def accueil(request):
	question_list_simple = Question.objects.filter(typeReponse_q="Choix simple")
	question_list_multiple = Question.objects.filter(typeReponse_q="Choix multiple")
	question_list_alphanumerique = Question.objects.filter(typeReponse_q="Choix alphanumerique")
	return render(request, 'appli/accueil.html' , { 'question_list_simple' : question_list_simple, 'question_list_multiple' : question_list_multiple, 'question_list_alphanumerique' : question_list_alphanumerique })



def choixquestion_view(request):
	if request.method=='POST':
		form = ChoixQuestion(request.POST)
		if form.is_valid:
			question = form.cleaned_data.get('question')
			#fecrire du code pour savoir ce que l on va faire
	else:
		form = ChoixQuestion
	return render(	request,'appli/ajout.html',
									{'form':form})
									#context_instance = RequestContext(request) )


def form_question(request):
	return render_to_response('appli/formQuestion.html')


#def error(request):
#	 return render('appli/connexionEnseigant.html')

