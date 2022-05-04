from django.db import models
import datetime


# Create your models here.
class ManagerAccountModel(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=60)
    password = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.id} - {self.login}"


class UserInfoModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    gender = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=16)
    passportNumber = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.id} - {self.surname}"


class DepartureInfoModel(models.Model):
    id = models.AutoField(primary_key=True)
    departureplace = models.CharField(max_length=60)
    departuredate = models.DateTimeField("Date", default=datetime.date.today)

    def __str__(self):
        return f"{self.id} - {self.departureplace}"


class AdditionalInfoModel(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=60)
    hotel = models.CharField(max_length=60)
    rating = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.id} - {self.country}"


class TourModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    price = models.CharField(max_length=10)
    nightamount = models.CharField(max_length=2)
    additionalinformation = models.ForeignKey(AdditionalInfoModel, on_delete=models.CASCADE)
    departureinformation = models.ForeignKey(DepartureInfoModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.name}"


class TicketModel(models.Model):
    id = models.AutoField(primary_key=True)
    tourinformation = models.ForeignKey(TourModel, on_delete=models.CASCADE)
    managerinformation = models.ForeignKey(ManagerAccountModel, on_delete=models.CASCADE)
    userinformation = models.ForeignKey(UserInfoModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
