from django.contrib import admin
from .models import Embti, Question, Choice

# Register your models here.
admin.site.register(Embti)
admin.site.register(Question)
admin.site.register(Choice)