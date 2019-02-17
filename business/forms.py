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

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'tax_id': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.TextInput(attrs={'class':'form-control'}),
            'zipcode': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'web': forms.TextInput(attrs={'class':'form-control'}),
            'fax': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }