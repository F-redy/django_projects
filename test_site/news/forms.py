from django import forms
from .models import Category


class AddNewsForm(forms.Form):
    title = forms.CharField(
        label='Название',
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название новости'}))

    content = forms.CharField(
        label='Текст',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Описание новости...'}))

    is_published = forms.BooleanField(label='Опубликовано', initial=True)

    cat = forms.ModelChoiceField(
        label='Категория',
        queryset=Category.objects.all(),
        empty_label='не выбрана',
        widget=forms.Select(attrs={'class': 'form-control'}))
