from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import  UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'size':'45','placeholder':'User Name'})
        self.fields['email'].widget = forms.TextInput(attrs={'size':'45','placeholder':'email id'})
        self.fields['username'].label = ""
        self.fields['email'].label = ""
        self.fields['password1'].widget = forms.TextInput(attrs={'size':'45','placeholder':'New Password should contain (A-Z,1-9 and @,#,$ )'})
        self.fields['password2'].widget = forms.TextInput(attrs={'size':'45','placeholder':'Confirm New Password'})

        self.fields['username'].help_text = ""
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""
        self.fields['password2'].label = ""
