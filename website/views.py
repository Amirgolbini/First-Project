from django.shortcuts import render


def index_page(request):
    return render(request, 'website/index.html')


def index1_page(request):
    return render(request, 'website/index1.html')


def index2_page(request):
    return render(request, 'website/index-2.html')

def index2light_page(request):
    return render(request, 'website/index-2-light.html')

def indexlight_page(request):
    return render(request, 'website/index-light.html')
