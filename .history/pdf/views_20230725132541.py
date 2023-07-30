from django.shortcuts import render, redirect
from .forms import ProfileForm

def accept(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('accept')
    return render(request, 'pdf/accept.html', {'form': form})
