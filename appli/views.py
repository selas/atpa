# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.shortcuts import render
from appli.models import Question
from appli.forms import Connexion, AjoutQuestion


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

				question_list_simple = Question.objects.filter(typeReponse_q="Choix simple")
				question_list_multiple = Question.objects.filter(typeReponse_q="Choix multiple")
				question_list_alphanumerique = Question.objects.filter(typeReponse_q="Choix alphanumerique")
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
		form = Connexion() # An unbound form
		return render(request, 'appli/connexion.html', {
			'form': form,
			})

		#if form.is_valid(): # All validation rules pass
			#Redirect to a success page.
		#	return HttpResponse("Connexion ok")
		#else:
			#Return a 'disabled account' error message 

def new_question(request):
	if request.method == 'POST': # If the form has been submitted...
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		form = Connexion(request.POST) # A form bound to the POST data

		if form.is_valid(): # All validation rules pass
			login(request, user)
			# Redirect to a success page.
			return render(request, 'appli/accueil.html')
		else:
			# Return a 'disabled account' error message
			return render(request, 'appli/connexion.html')
	else:
		form = AjoutQuestion() # An unbound form
		return render(request, 'appli/formQuestion.html', {
			'form': form,
			})


def home(request,name=None):
	if (name):
		return HttpResponse("test hello world !!!! %s" % name)
	else:
		return HttpResponse("Hello World")


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

