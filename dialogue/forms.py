from django import forms
from .models import Dialogue

class DialogueForm(forms.ModelForm):

    class Meta:
        model = Dialogue
        fields = ('question', )