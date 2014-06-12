# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

#from appli.views import  connexion, new_question

urlpatterns = patterns('',

	url(r'^accueil/$', 'appli.views.accueil', name='accueil'),
	url(r'^accueil/(?P<question_id>\w{1,4})/$', 'appli.views.affichageQuestion', name='affichageQuestion'),
	url(r'^question/(?P<question_posee_id>\w{1,4})/$', 'appli.views.question_posee', name='question_posee'),

	url(r'^question_en_ligne/$', 'appli.views.question_en_ligne', name='question_en_ligne'),
	url(r'^connexion/$', 'appli.views.connexion', name='connexion'),
	url(r'^deconnexion/$', 'appli.views.deconnexion', name='deconnexion'),
	url(r'^new_question/$', 'appli.views.new_question', name='new_question'),

	#url(r'^error/$', 'appli.views.error', name='error')
)