from .models import NewsArticles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class NewsArticlesForm(ModelForm):

    class Meta:

        model = NewsArticles
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            'title': TextInput(attrs={
                'class': 'mb-4 form form-control',
                'placeholder': 'Название статьи',
            }),
            'anons': TextInput(attrs={
                'class': 'mb-4 form form-control',
                'placeholder': 'Анонс статьи',
            }),
            'full_text': Textarea(attrs={
                'class': 'mb-4 form form-control',
                'placeholder': 'Текст статьи',
            }),
            'date': DateTimeInput(attrs={
                'class': 'mb-4 form form-control',
                'type': 'datetime-local',
                'placeholder': 'Дата публикации',
            }),
        }
