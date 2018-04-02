from    django import forms
from .models import *
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

        # 字段的帮助 提示信息
        help_texts = {
            'hostname': '*  必填项目,名字唯一',
        }


        # 二级联动选项的样式
        widgets = {
            'country': forms.Select(
                attrs={'class': 'select2',
                       'data-placeholder': ('----请选择国家----')}),
            'city': forms.Select(
                attrs={'class': 'select2',
                       'data-placeholder': ('----请选择城市----')}),
        }

    # 二级联动相关
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')


########################################################################################################################
## 添加映射
########################################################################################################################
class AddPortMapForm(forms.ModelForm):
    class Meta:
        model = PortMap
        fields = '__all__'