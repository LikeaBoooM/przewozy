from django import forms
from . models import Przewoz


class DateInput(forms.DateInput):
    input_type = 'date'

    
class PrzewozysForm(forms.Form):
    class Meta:
        model = Przewoz
        fields = ['carrier',
                  'plate_number',
                  'client',
                  'product',
                  'wage_without_car']


class PrzewozForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Przewoz
        fields = ['carrier',
                  'plate_number',
                  'client',
                  'product',
                  'wage_without_car']
