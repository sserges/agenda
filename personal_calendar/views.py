from django.shortcuts import render, HttpResponseRedirect

from .forms import EventForm
from .models import Evenement

def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/agenda/create/')
    else:
        form = EventForm()
    
    return render(request, 'event/create.html', {'form':form})


def details(request, id):
    event = Evenement.objects.get(pk=id)
    return render(request, 'event/details.html', {'event':event})