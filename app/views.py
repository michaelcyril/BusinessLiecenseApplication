from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')


def start_request(request):
    return render(request, 'ombi_jipya.html')


def request_details(request):
    return render(request, 'endeleza_ombi.html')


def request_followup(request):
    return render(request, 'ufatiliaji_ombi.html')


def address_saving(request):
    if request.method != "POST":
        return render(request, 'taarifa_za_makazi.html')
    else:
        try:
            data = request.POST
            user = User.objects.get(id=data['user'])
            address = AddressInformation.objects.create(
                user=user,
                nida=data['nida'],
                fist_name=data['first_name'],
                middle_name=data['middle_name'],
                last_name=data['last_name'],
                region=data['region'],
                district=data['district'],
                ward=data['ward'],
                village=data['village'],
                phone=data['phone'],
                email=data['email']
            )
            address.save()
            return render(request, 'taarifa_za_biashara.html')
        except:
            return render(request, 'taarifa_za_makazi.html', {'message': 'Fail to save'})



def tra_saving(request):
    if request.method != "POST":
        return render(request, 'taarifa_za_biashara.html')
    else:
        try:
            data = request.POST
            user = User.objects.get(id=data['user'])
            tra = TraInformation.objects.create(
                user=user,
                tin=data['tin'],
                requester=data['requester'],
                posta=data['posta'],
                region=data['region'],
                district=data['district'],
                ward=data['ward'],
                village=data['village'],
                lisence_number=data['lisence_number'],
                business=data['business']
            )
            tra.save()
            return render(request, 'control_number.html')
        except:
            return render(request, 'taarifa_za_biashara.html')


def control_saving(request):
    if request.method != "POST":
        user = User.objects.get(username=request.user)
        control = ControlNumber.objects.get(user=user)
        message = {'control_number': control.control_number, 'is_paid': control.is_paid}
        return render(request, 'control_number.html', message)

    else:
        try:
            data = request.POST
            control = ControlNumber.objects.get(control_number=data['control_number'])
            control.is_paid = True
            return render(request, 'download_pdf.html')
        except:
            return render(request, 'control_number.html')
