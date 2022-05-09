from django.db import models


# Create your models here.
class DepartureInfoModel(models.Model):
    id = models.AutoField(primary_key=True)
    departureplace = models.CharField(max_length=60, null=True)
    departuredate = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.id} - {self.departureplace}"


class AdditionalInfoModel(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=60, null=True)
    hotel = models.CharField(max_length=60, null=True)
    rating = models.CharField(max_length=5, null=True)

    def __str__(self):
        return f"{self.id} - {self.country}"


class TourModel(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/', null=True)
    name = models.CharField(max_length=60, null=True)
    price = models.CharField(max_length=10, null=True)
    nightamount = models.CharField(max_length=2, null=True)
    description = models.TextField(null=True)
    additionalinformation = models.ForeignKey(
        AdditionalInfoModel, on_delete=models.CASCADE
    )
    departureinformation = models.ForeignKey(
        DepartureInfoModel, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.id} - {self.name}"


class TicketModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    surname = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=60, null=True)
    gender = models.CharField(max_length=30, null=True)
    phoneNumber = models.CharField(max_length=16, null=True)
    passportNumber = models.CharField(max_length=12, null=True)
    tourinformation = models.ForeignKey(TourModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.surname}"