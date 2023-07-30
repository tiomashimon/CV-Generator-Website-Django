from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io


def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        summary = request.POST.get('summary')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        previous_job = request.POST.get('previous_job')
        skills = request.POST.get('skills')

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school,
                          university=university, previous_job=previous_job, skills=skills)
        profile.save()

    return render(request, 'pdf/accept.html')


def cv(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/cv.html')
    html = template.render({'user_profile': user_profile})
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response


def list_of_cv(request):
    cv_objects = Profile.objects.all()

    return render(request, 'pdf/list.html', {'cv_objects': cv_objects})


def home(request):
    return render(request, 'pdf/home.html')
