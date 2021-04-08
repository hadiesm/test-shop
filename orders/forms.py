from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','address',
                  'postal_code','city']

    def __init__(self,*args,**kwargs):
        super(OrderForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Last Name'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
        self.fields['address'].widget.attrs.update({'class':'form-control','placeholder':'Address'})
        self.fields['postal_code'].widget.attrs.update({'class':'form-control','placeholder':'ZIP Code'})
        self.fields['city'].widget.attrs.update({'class':'form-control','placeholder':'City'})
