from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_page(request):
    data = {
        'title': 'Главная страница!!!',
        'values': ['some', 'hello', '123']
    }
    return render(request, 'labssite/index.html', data)


def about(request):
    return render(request, 'labssite/about.html')
