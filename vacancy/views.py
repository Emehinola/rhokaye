from django.shortcuts import render
from .models import Vacancy
from .forms import Application
from django import forms
from django.contrib import messages

def vacancy(request):
    vacancies = Vacancy.objects.all()
    context = {
        'vacancies': vacancies,
        'title': 'vacancy'
    }

    return render(request, 'vacancy/vacancy.html', context)

def application(request):
    if request.method == "POST":
        form = Application(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "You have successfully submitted your application... monitor your email for updates. Thanks")

        else:
            raise forms.ValidationError("Error, make sure you fill all fields correctly")

    else:
        form = Application()

    contex = {
        'title':'Application',
        'form':form
    }

    return render(request, 'vacancy/applications.html', contex)
