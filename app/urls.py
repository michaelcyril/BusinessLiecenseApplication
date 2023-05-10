from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('/ombi_jipya', start_request, name='start'),
    path('/endeleza_ombi', request_details),
    path('/fuatilia_ombi', request_followup, name='followup')
]