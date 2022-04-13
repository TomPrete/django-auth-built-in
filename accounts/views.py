from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/signup.html'

