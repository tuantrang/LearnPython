from django.shortcuts import render, redirect
from .models import TimeEntry
from .forms import TimeEntryForm

def homepage(request):
    time_entries = TimeEntry.objects.all()
    context = {"time_entries": time_entries}
    return render(request,'mytime/index.html', context)

def about(request):
    return render(request,'mytime/about.html')


def create_time_entry(request):
    form = TimeEntryForm()
    if request.method == 'POST':
        form = TimeEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'mytime/time_entry_form.html',  context)

def update_time_entry(request, pk):
    time_entry = TimeEntry.objects.get(id=pk)
    form = TimeEntryForm(instance=time_entry)
    if (request.method == 'POST'):
        form = TimeEntryForm(request.POST, instance=time_entry)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"form": form}

    return render(request, 'mytime/time_entry_form.html', context )
    