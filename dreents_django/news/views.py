from django.shortcuts import render, redirect
from .models import NewsArticles
from .forms import NewsArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_main(request):
    news = NewsArticles.objects.order_by('date')
    return render(request, 'news/news_main.html', {'news': news})


def add_entry(request):
    error = ''
    if request.method == 'POST':
        form = NewsArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма заполнена неверно.'
    form = NewsArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/add_entry.html', data)


class NewsArticleDetail(DetailView):

    model = NewsArticles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


class NewsArticleEdit(UpdateView):

    model = NewsArticles
    template_name = 'news/add_entry.html'
    form_class = NewsArticlesForm


class NewsArticleDelete(DeleteView):

    model = NewsArticles
    template_name = 'news/article_delete.html'
    success_url = '/news/'
