from django.contrib import admin

from .models import Question, Employee

admin.site.register(Question)

from .models import Choice

admin.site.register(Choice)

admin.site.register(Employee)