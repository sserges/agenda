from django.contrib import admin

from .models import Evenement, Evenement_Participant

# Register your models here.

admin.site.register(Evenement)
admin.site.register(Evenement_Participant)
