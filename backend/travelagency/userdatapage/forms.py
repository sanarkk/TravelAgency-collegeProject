from django.forms import ModelForm
from mainpage.models import UserInfoModel, TicketModel


class CustomerForm(ModelForm):
    class Meta:
        model = UserInfoModel
        fields = '__all__'


class TicketForm(ModelForm):
    class Meta:
        model = TicketModel
        fields = '__all__'