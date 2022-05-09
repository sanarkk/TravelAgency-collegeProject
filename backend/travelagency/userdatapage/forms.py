from django.forms import ModelForm
from mainpage.models import TicketModel

class TicketForm(ModelForm):
    class Meta:
        model = TicketModel
        fields = '__all__'