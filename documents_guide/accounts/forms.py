from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserProfileCreationForm(UserCreationForm):
    """
    Kullanıcı kaydı için özel form
    """
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = UserProfile  # UserProfile modelini kullanalım
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'address')

    def save(self, commit=True):
        userprofile = super().save(commit=False)  # UserProfile'ı kaydediyoruz
        if commit:
            userprofile.save()

        return userprofile
