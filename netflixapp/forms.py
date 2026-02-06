from django.forms import ModelForm
from netflixapp.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields=['name','age','age_limit']