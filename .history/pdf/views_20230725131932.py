from django.shortcuts import render
from .forms import ProfileForm

def accept(request):
    return render(request, 'pdf/accept.htlm', for)
