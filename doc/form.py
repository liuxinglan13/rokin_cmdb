from    django import forms
from .models import Doc
from markdown.forms import MarkdownField

class DocForm(forms.ModelForm):

    doc_body = MarkdownField()

    class Meta:
        model = Doc
        fields = '__all__'

