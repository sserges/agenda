from django.forms import ModelForm

from .models import Evenement, Evenement_Participant

class EventForm(ModelForm):

    class Meta:
        model = Evenement
        exclude = ["participants"]


class Evenement_ParticipantForm(ModelForm):

    class Meta:
        model = Evenement_Participant
        exclude = []