from django import forms
from .models import FAQ
from ckeditor.widgets import CKEditorWidget

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']
        widgets = {
            'question': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'answer': CKEditorWidget(),
        }
