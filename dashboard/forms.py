from django import forms
from django.forms import widgets
from . models import *
from django.contrib.auth.forms import  UserCreationForm


class NotesForm(forms.ModelForm):
    class Meta:
        model  = Notes
        fields = ['title', 'description']

class DateInput(forms.DateInput):
    input_type = 'date'


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}
        fields = ['subject', 'title','description', 'due','is_finished']


class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100,label="Enter your search:")


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished']


class ConversionForm(forms.Form):
    CHOICES = [('length', 'Length'), ('mass', 'Mass')]
    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


class ConversionLengthForm(forms.Form):
    CHOICES = [('pound','pound'),('kilogram','kilogram')]
    input=forms.CharField(
        required=False,
        label='Input Value',
        widget=forms.TextInput(attrs = {
            'type':'number',
            'placeholder':'Enter the Number'
        })
    )
     
    measure1 = forms.CharField(
        label="form unit",
        widget = forms.Select(choices = CHOICES)
    )
    
    measure2 = forms.CharField(
        label="To Unit",
        widget = forms.Select(choices = CHOICES)
    )
 


class ConversionMassForm(forms.Form):
    CHOICES = [('pound','pound'),('kilogram','kilogram')]

    input=forms.CharField(
        required=False,
        label="Input Value",
        widget=forms.TextInput(attrs ={
            'type':'number',
            'placeholder':'Enter the Number'

        })
    )
     
    measure1 = forms.CharField(
        label='From Unit',
        widget = forms.Select(choices = CHOICES)
    )
    
    measure2 = forms.CharField(
        label='To Unit',
        widget = forms.Select(choices = CHOICES)
    )


class UserRegistrationForm(UserCreationForm):
    class meta:
        model =User
        fields = ['username','password1','password2']
        