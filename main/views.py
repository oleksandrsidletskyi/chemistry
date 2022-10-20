from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about-us.html')


def organic(request):
    return render(request, 'main/organic.html')


def izomery(request):
    return render(request, 'main/izomery.html')


def alkany(request):
    return render(request, 'main/alkany.html')


def alkeny(request):
    return render(request, 'main/alkeny.html')


def alkiny(request):
    return render(request, 'main/alkiny.html')

