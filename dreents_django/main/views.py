from django.shortcuts import render


def index(request):
    data = {
        'h1_content': 'Вы на главной странице сайта!',
        'values': ['Some', 'text', 'for', 'this', 'page', '!'],
        'objects_dict': {
            'name': 'Василий',
            'age': 23,
            'username': 'DreenTS',
        },
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
