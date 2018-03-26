from    django import forms
from .models import assets
from markdown.forms import MarkdownField

class AssetForm(forms.ModelForm):

    # ps = MarkdownField()

    class Meta:
        model = assets
        fields = '__all__'

        labels={
            "network_ip":"IP",
        }
        error_messages = {
            'model':{
                'max_length': ('太短了'),
            }
        }
