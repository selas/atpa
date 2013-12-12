# -*- coding: utf-8 -*-

from django.contrib import admin
from appli.models import Question, Question_reponse, Question_posee, Reponse_saisie

admin.site.register(Question)
admin.site.register(Question_reponse)
admin.site.register(Question_posee)
admin.site.register(Reponse_saisie)



