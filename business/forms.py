from django import forms
from .models import Business

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business

        fields = [
            'name',
            'tax_id',
            'address',
            'city',
            'state',
            'zipcode',
            'phone',
            'web',
            'fax',
            'email',
        ]

        labels = {
            'name':'Name',
            'tax_id':'Tax ID',
            'address':'Address',
            'city':'City',
            'state':'State',
            'zipcode':'Zipcode',
            'phone':'Phone',
            'web':'Web',
            'fax':'Fax',
            'email':'Email',
        }