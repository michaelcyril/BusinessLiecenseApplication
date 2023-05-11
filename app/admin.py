from django.contrib import admin
from .models import *

# Register your models here.

model = [User, TraInformation, AddressInformation]
for data in model:
    admin.site.register(data)