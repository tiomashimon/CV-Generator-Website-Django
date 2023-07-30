from django.shortcuts import render
from .forms import ProfileForm

def accept(request):
    form = ProfileForm(request.Pos)
    return render(request, 'pdf/accept.htlm', for)
