from django.shortcuts import render, redirect

from .forms import NoteModelForm
from .models import Note

# CRUD(create, retrieve, update, delete) implementation

# Function-based view


def create_view(request):
    # Only POST request is accepted in this case
    form = NoteModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, "notepad/create.html", context)
