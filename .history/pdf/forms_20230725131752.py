from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'email', 'phone', 'summary', 'degree', 'university', 'previous_job', 'university')
         name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previous_job = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)