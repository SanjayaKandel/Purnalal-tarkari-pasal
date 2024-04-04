from django import forms
from. models import vegetable, fruit

class VegetableRegistrationForm(forms.ModelForm):
    class Meta:
        model = vegetable
        fields = ['name', 'quantity', 'price']

class UpdateVegetableForm(forms.ModelForm):
    class Meta:
        model = vegetable
        fields = ['name', 'quantity', 'price']
        
class FruitRegistrationForm(forms.ModelForm):
    class Meta:
        model = fruit
        fields = ['name', 'quantity', 'price']
        
class UpdateFruitForm(forms.ModelForm):
    class Meta:
        model=fruit
        fields = ['name', 'quantity', 'price']