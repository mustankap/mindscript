from django import forms
from .models import *

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ('type', 'price', 'status', 'issues')

class ConcreteForm(forms.ModelForm):
    class Meta:
        model = Concrete
        fields = ('type', 'price', 'status', 'issues')

class InsulationForm(forms.ModelForm):
    class Meta:
        model = Insulation
        fields = ('type', 'price', 'status', 'issues')

class Electrical_wiringForm(forms.ModelForm):
    class Meta:
        model = Electrical_wiring
        fields = ('type', 'price', 'status', 'issues')

class CementForm(forms.ModelForm):
    class Meta:
        model = Cement
        fields = ('type', 'price', 'status', 'issues')

class PlasterForm(forms.ModelForm):
    class Meta:
        model = Plaster
        fields = ('type', 'price', 'status', 'issues')

class CeilingForm(forms.ModelForm):
    class Meta:
        model = Ceiling
        fields = ('type', 'price', 'status', 'issues')

class PaintForm(forms.ModelForm):
    class Meta:
        model = Paint
        fields = ('type', 'price', 'status', 'issues')

class Fire_suppression_equipForm(forms.ModelForm):
    class Meta:
        model = Fire_suppression_equip
        fields = ('type', 'price', 'status', 'issues')

class HVACForm(forms.ModelForm):
    class Meta:
        model = HVAC
        fields = ('type', 'price', 'status', 'issues')

class MasonryForm(forms.ModelForm):
    class Meta:
        model = Masonry
        fields = ('type', 'price', 'status', 'issues')

class PlasticForm(forms.ModelForm):
    class Meta:
        model = Plastic
        fields = ('type', 'price', 'status', 'issues')

class PlumbingForm(forms.ModelForm):
    class Meta:
        model = Plumbing
        fields = ('type', 'price', 'status', 'issues')
