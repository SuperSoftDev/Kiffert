from django import forms
from .models import Users
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import validate_email

def validate_password_strength(password):
    min_length = 8
    errors = []
    flag = False

    if len(password) < min_length:
        errors.append(_('Password must be at least {0} characters '
                                'long.').format(min_length))
        flag = True

    # check for 2 digits
    if not any(c.isdigit() for c in password):
        errors.append('Password must contain at least 1 digit.')
        flag = True

    # check for uppercase letter
    if not any(c.isupper() for c in password):
        errors.append('Password must contain at least 1 uppercase letter.')
        flag = True

    # check for uppercase letter
    if not any(c.islower() for c in password):
        errors.append('Password must contain at least 1 lowecase letter.')
        flag = True
    if flag:
        raise ValidationError(errors)
    return password
    
class SignupForm(forms.Form):
    email = forms.CharField(max_length=100,required=True)
    password = forms.CharField(max_length=100,required=True)
    confirm = forms.CharField(max_length=100,required=True)

    class Meta:
        model = Users
        fields = ("email",'password')
    def save(self):
        user = Users()
        user.email = self.cleaned_data.get("email")
        user.password = make_password(self.cleaned_data.get("password"))
        return user
    def clean_password(self):
        return validate_password_strength(self.cleaned_data['password'])

    def clean_confirm(self):
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password != confirm:
            raise forms.ValidationError(_("The password does not match the confirm password."))
        return confirm
    
    def clean_email(self):
        try:
            validate_email(self.cleaned_data['email'])
        except:
            raise forms.ValidationError(_("Invalid Email Address."))
        if Users.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields["email"].required = True
class LoginForm(forms.Form):
    email = forms.CharField(max_length=100,required=True)
    password = forms.CharField(max_length=100,required=True)

    def clean_email(self):
        if (Users.objects.filter(email__iexact=self.cleaned_data['email']).count()==0):
            raise forms.ValidationError(_("Email doesn't exist."))
        return self.cleaned_data['email']
    def clean_password(self):
        user = Users.objects.filter(email__iexact=self.cleaned_data.get('email'))
        if(user.count()==0):
            return ''
        print(user[0].password)
        print(self.cleaned_data.get('password'))
        if(check_password(self.cleaned_data['password'],user[0].password) == False):
            raise forms.ValidationError(_("Password isn't correct."))
        return ''
