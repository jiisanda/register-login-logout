from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user_auth_app.models import UserProfileInfo

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name *'}), label=False)
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name *'}), label=False)
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username *'}), label=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email *'}), label=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}), label=False)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}), label=False)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')



class UserProfileInfoForm(forms.ModelForm):
    DOCTOR = 1
    PATIENT = 2
    ROLE_CHOICES = (
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient'),
    )
    role = forms.ChoiceField(choices = ROLE_CHOICES)
    profile_picture = forms.ImageField()
    address_line1 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3', 'placeholder':'Address in 1 Line'}), label=False)
    address_city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), label=False)
    address_state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), label=False)
    address_pincode = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Pincode'}), label=False)
    class Meta:
        model = UserProfileInfo
        fields = ('role', 'profile_picture', 'address_line1', 'address_city', 'address_state', 'address_pincode')

