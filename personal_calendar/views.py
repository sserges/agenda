from django.shortcuts import render, HttpResponseRedirect

from .forms import EventForm


def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/agenda/create/')
    else:
        form = EventForm()
    
    return render(request, 'event/create.html', {'form':form})