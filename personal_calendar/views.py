from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.forms import HiddenInput

from .forms import EventForm, Evenement_ParticipantForm
from .models import Evenement, Evenement_Participant

def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return HttpResponseRedirect('/agenda/%i/details/' % event.pk)
    else:
        form = EventForm()
    
    return render(request, 'event/create.html', {'form':form})


def details(request, id):
    event = Evenement.objects.get(pk=id)
    if request.method == "POST":
        form = Evenement_ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/agenda/%s/details/' % id)
    else:
        form = Evenement_ParticipantForm(initial={'evenement':event})
        participants = [user.pk for user in event.participants.all()]
        form.fields['participant'].queryset=User.objects.exclude(
            pk__in=participants
        )
        form.fields['evenement'].widget = HiddenInput()

    return render(request, 'event/details.html', {
        'event':event,
        'form':form
    })


def delete_participant(request, id_event, id_participant):
    if request.method == "POST":
        evenement = Evenement.objects.get(pk=id_event)
        participant = User.objects.get(pk=id_participant)
        a_supprimer = Evenement_Participant.objects.get(
            evenement=evenement,
            participant=participant
        )
        
        a_supprimer.delete()
    return HttpResponseRedirect('/agenda/%s/details/' % id_event)
