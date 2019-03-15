from django.shortcuts import render, render_to_response
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, ListView, DetailView
from survey import models


# Create your views here.

def index(request):
    return render(request, 'survey/home.html')


def login(request):
    return render(request, 'survey/login.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                return render(request, 'survey/survey_home.html', {})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'survey/login.html', {})


class EmployeeSurveys(LoginRequiredMixin, ListView):
    context_object_name = 'UsersSurveys'
    model = models.UsersSurveys
    template_name = 'survey/survey_home.html'

    def get_queryset(user):
        return models.objects.filter(user=user.request.user)
