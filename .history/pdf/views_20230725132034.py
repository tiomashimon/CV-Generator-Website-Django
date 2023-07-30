from django.shortcuts import render
from .forms import ProfileForm

def accept(request):
    form = ProfileForm(request.POST or None)
    return render(request, 'pdf/accept.htlm', for)
    if fo
