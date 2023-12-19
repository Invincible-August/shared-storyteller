from django.shortcuts import render


def index(request):
    context = {}
    context['hello'] = '你好!'
    return render(request, 'index.html', context)