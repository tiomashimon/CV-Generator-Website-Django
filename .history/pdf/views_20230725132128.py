from django.shortcuts import render, redirect
from .forms import ProfileForm

def accept(request):
    form = ProfileForm(request.POST or None)
    return render(request, 'pdf/accept.htlm', for)
    if form.is_valid():
        form.save()
        return redirect('accept')
