from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import Customer, Product

UPLOADCARE_PUBLIC_KEY = '76122001cca4add87f02'  # Badilisha kama una key nyingine

from . import models

from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_image'].widget.attrs.update({
            'role': 'uploadcare-uploader',
            'data-public-key': UPLOADCARE_PUBLIC_KEY,
        })



class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        


#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_pic'].widget.attrs.update({
            'role': 'uploadcare-uploader',
            'data-public-key': UPLOADCARE_PUBLIC_KEY,
        })

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_image'].widget.attrs.update({
            'role': 'uploadcare-uploader',
            'data-public-key': UPLOADCARE_PUBLIC_KEY,
        })
        self.fields['category'].empty_label = "Select Category"
