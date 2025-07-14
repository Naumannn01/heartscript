from django.shortcuts import render, redirect
from .forms import LoveNoteForm
from .models import LoveNote
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random

def create_note(request):
    if request.method=='POST':
        form=LoveNoteForm(request.POST)
        if form.is_valid():
            note=form.save(commit=False)
            note.user=request.user
            note.generated_text = generate_letter(note.to_name, note.mood, note.memory)
            note.save()
            messages.success(request, "💌 Your love letter has been created!")
            return redirect('my_notes')
    else:
        form=LoveNoteForm()
    return render(request, 'lovenotes/create_note.html', {'form':form})