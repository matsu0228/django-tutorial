from django.shortcuts import render
from .models import Dialogue
from .forms import DialogueForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

def dialogue_detail(request, pk):
    dialogue = get_object_or_404(Dialogue, pk=pk)
    return render(request, 'dialogue/dialogue_detail.html', {'dialogue': dialogue})

def dialogue_new(request):
    if request.method == "POST":
        form = DialogueForm(request.POST)
        if form.is_valid():
            dialogue = form.save(commit=False)
            dialogue.author = request.user
            dialogue.save()
            return redirect(dialogue_detail, pk=dialogue.pk)
    else:
        form = DialogueForm()
        return render(request, 'dialogue/dialogue_detail.html', {'dialogue': dialogue})

def dialogue_remove(request, pk):
    dialogue = get_object_or_404(Dialogue, pk=pk)
    dialogue.delete()
    return redirect('dialogue_list')
