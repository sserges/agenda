from django.forms import ModelForm

from .models import Evenement

class EventForm(ModelForm):

    class Meta:
        model = Evenement
        exclude = ["participants"]
