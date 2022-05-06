from django.forms import ModelForm
from mainpage.models import ManagerAccountModel
from mainpage.models import ManagerAccountModel


class LoginForm(ModelForm):
    class Meta:
        model = ManagerAccountModel
        fields = [
            'login',
            'password'
        ]
