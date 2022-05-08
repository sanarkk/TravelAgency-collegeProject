from django.forms import ModelForm
from mainpage.models import UserInfoModel


class CustomerForm(ModelForm):
    class Meta:
        model = UserInfoModel
        fields = '__all__'
