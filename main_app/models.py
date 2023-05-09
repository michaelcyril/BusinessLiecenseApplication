from django.db import models


# Create your models here.
class User(models.Model):
    phone = models.CharField(max_length=12)
    current_region = models.CharField(max_length=20)
    office_region = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        db_table = "user"


class AddressInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nida = models.CharField(max_length=20)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    ward = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nida}'

    class Meta:
        db_table = "addressInformation"


class TraInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tin = models.CharField(max_length=20)
    requester = models.CharField(max_length=200)
    posta = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    district = models.CharField(max_length=30)
    ward = models.CharField(max_length=200)
    village = models.CharField(max_length=30)
    lisence_number = models.CharField(max_length=200)
    business = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.tin}'

    class Meta:
        db_table = "traInformation"


# For the dummy data

class Tra(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tin = models.CharField(max_length=20)
    requester = models.CharField(max_length=200)
    posta = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    district = models.CharField(max_length=30)
    ward = models.CharField(max_length=200)
    village = models.CharField(max_length=30)
    lisence_number = models.CharField(max_length=200)
    business = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.tin}'

    class Meta:
        db_table = "tra"

