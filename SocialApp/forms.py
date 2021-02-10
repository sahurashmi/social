from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False)#, help_text='Optional.')
    email = forms.EmailField(max_length=254)#, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2', )


class SocialIssueForm(ModelForm):
    campaign_title = forms.CharField(max_length=30, required=True)
    description = forms.Textarea()

    class Meta:
        model = SocialIssue
        fields = ('campaign_title','image', 'description')


class BusinessModelForm(ModelForm):

    description = forms.Textarea()
    contact_number = forms.IntegerField()
    # campaign_title = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         'maxlength': '255',
    #     })
    # )
    class Meta:
        model = BusinessPost
        fields = ('company_name','campaign_title','description','image','address','contact_number')
