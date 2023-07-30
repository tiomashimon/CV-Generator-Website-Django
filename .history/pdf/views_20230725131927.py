from django.shortcuts import render
from .forms import Pr

def accept(request):
    return render(request, 'pdf/accept.htlm')
