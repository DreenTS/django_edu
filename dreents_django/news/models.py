from django.db import models


class NewsArticles(models.Model):

    title = models.CharField('Название статьи', max_length=60)
    anons = models.CharField('Анонс статьи', max_length=200)
    full_text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:

        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
