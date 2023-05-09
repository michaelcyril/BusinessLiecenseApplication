from django.shortcuts import render

# Create your views here.


def my_view(request):
    # do some processing here
    context = {'foo': 'bar'}
    return render(request, 'base.html', context)

