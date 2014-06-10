# -*- coding: utf-8 -*-

from django.contrib import admin
from appli.models import Question, Reponse, Question_ligne, Reponse_ligne, Type

admin.site.register(Question)
admin.site.register(Type)
admin.site.register(Reponse)
admin.site.register(Question_ligne)
admin.site.register(Reponse_ligne)



