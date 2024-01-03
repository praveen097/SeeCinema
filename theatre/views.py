# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TheatreForm
from .models import Theatre

def add_theatre(request):
    if request.method == 'POST':
        form = TheatreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_theatres')  # Redirect to a success page
    else:
        form = TheatreForm()

    return render(request, 'theatre/add_theatre.html', {'form': form})

def all_theatres(request):
    theatres = Theatre.objects.all()
    return render(request, 'theatre/all_theatres.html', {'theatres': theatres})

def edit_theatre(request, theatre_id):
    theatre = get_object_or_404(Theatre, pk=theatre_id)

    if request.method == 'POST':
        form = TheatreForm(request.POST, request.FILES, instance=theatre)
        if form.is_valid():
            form.save()
            return redirect('all_theatres')  # Redirect to the page displaying all theatres
    else:
        form = TheatreForm(instance=theatre)

    return render(request, 'theatre/edit_theatre.html', {'form': form, 'theatre': theatre})

def view_theatre(request, theatre_id):
    theatre = get_object_or_404(Theatre, pk=theatre_id)
    return render(request, 'theatre/view_theatre.html', {'theatre': theatre})

def delete_theatre(request, theatre_id):
    theatre = get_object_or_404(Theatre, pk=theatre_id)
    
    if request.method == 'POST':
        theatre.delete()
        return redirect('all_theatres')  # Redirect to the page displaying all theatres

    return render(request, 'theatre/delete_theatre.html', {'theatre': theatre})