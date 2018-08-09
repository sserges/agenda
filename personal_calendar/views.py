from django.shortcuts import render, HttpResponseRedirect, render_to_response, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.forms import HiddenInput
from django.template.loader import render_to_string
from django.template import RequestContext
import json

from .forms import EventForm, Evenement_ParticipantForm
from .models import Evenement, Evenement_Participant

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return HttpResponseRedirect('/agenda/%i/details/' % event.pk)
    else:
        form = EventForm()
    
    return render(request, 'event/create.html', {'form':form})


def event_details(request, id):
    event = Evenement.objects.get(pk=id)

    if request.method == "POST":
        form = Evenement_ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                delete_form = render_to_string(
                    'blocks/delete_form.html',
                    {'delete_url': form.instance.delete_url()},
                    request
                )

                data = {
                    'participant': form.instance.participant.username,
                    'get_status_display': form.instance.get_status_display(),
                    'delete_form': delete_form
                }

                form = Evenement_ParticipantForm(initial={'evenement':event})
                participants = [user.pk for user in event.participants.all()]
                form.fields['participant'].queryset=User.objects.exclude(
                    pk__in=participants
                 )
                form.fields['evenement'].widget = HiddenInput()
                participant_form = render_to_string(
                    'blocks/participant_form.html',
                    {'form':form},
                    request
                )

                data['participant_form'] = participant_form

                return JsonResponse(data)
                
            return HttpResponseRedirect('/agenda/%s/details/' % id)
    else:
        form = Evenement_ParticipantForm(initial={'evenement':event})
        participants = [user.pk for user in event.participants.all()]
        form.fields['participant'].queryset=User.objects.exclude(
            pk__in=participants
        )
        form.fields['evenement'].widget = HiddenInput()

    if request.is_ajax():
        print('ajax2')
        return render_to_response(
            'blocks/participant_form.html',
            {
                'event':event,
                'form':form
            }
        )

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

        # if request.is_ajax():
        #     return HttpResponseRedirect('/agenda/%s/details/' % id_event)
            
    return HttpResponseRedirect('/agenda/%s/details/' % id_event)


def list_event(request):
    events = Evenement.objects.all()
    return render(request, 'event/list.html', {"events":events})


def delete_event(request, id):
    if request.method == "POST":
        event = Evenement.objects.get(pk=id)
        event.delete()
        return HttpResponseRedirect('/agenda/list/')


def update_event(request, id):
    event = Evenement.objects.get(pk=id)
    if request.method == "POST":
        print(request.POST)
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/agenda/%i/details/' % event.pk)
    else:
        form = EventForm(instance=event)
    
    return render(request, 'event/create.html', {'form':form})

