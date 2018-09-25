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


def list_view(request):
    notes = Note.objects.all()
    context = {
        'object_list': notes
    }
    return render(request, "notepad/list.html", context)


def delete_view(request, id):
    item_to_delete = Note.objects.filter(pk=id)  # return a list
    if item_to_delete.exists():
        if request.user == item_to_delete[0].user:
            item_to_delete[0].delete()
    return redirect('notes/list')
