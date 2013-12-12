# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

#from appli.views import  connexion, new_question

urlpatterns = patterns('',
	#url(r'^home/$', 'appli.views.home', name='home'),
	#url(r'^home/(\w+)?$', 'appli.views.home', name='home_name'), 

	url(r'^accueil/$', 'appli.views.accueil', name='accueil'),
	#url(r'^form_question/$', 'appli.views.form_question', name='form_question'),
	url(r'^connexion/$', 'appli.views.connexion', name='connexion'),
	url(r'^new_question/$', 'appli.views.new_question', name='new_question'),

	#url(r'^error/$', 'appli.views.error', name='error')
)
