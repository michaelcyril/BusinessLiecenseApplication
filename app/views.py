from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def start_request(request):
    return render(request, 'ombi_jipya.html')


def request_details(request):
    return render(request, 'endeleza_ombi.html')


def request_followup(request):
    return render(request, 'ufatiliaji_ombi.html')