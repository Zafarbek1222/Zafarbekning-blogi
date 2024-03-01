from django.views.generic import TemplateView
from django.shortcuts import render
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


def signupcss(request):
    return render(request, 'signup.html')

def loginimagecss(request):
    return render(request, 'login.html')
