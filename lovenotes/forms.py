from django import forms
from . models import LoveNote

class LoveNoteForm(forms.ModelForm):
    class Meta:
        model = LoveNote
        fields = [
            'to_name','mood','memory'
        ]
        widgets={
            'memory':forms.Textarea(attrs={'rows':3}),
        }