import re

from django import forms
from django.core.exceptions import ValidationError

from .models import News


class AddNewsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddNewsForm, self).__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = News
        fields = ('title', 'content', 'is_published', 'cat')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название новости'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Описание новости...'}),
            'cat': forms.Select(attrs={'class': 'form-control'}),

        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название новости не должно начинаться с цифры')
        return title
