from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def properties(request):
    return render(request, 'properties.html')


def properties_single(request):
    return render(request, 'properties-single.html')


def blog_single(request):
    return render(request, 'single.html')
