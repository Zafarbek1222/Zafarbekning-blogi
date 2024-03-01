from django.urls import path
from .views import HomePageView, signupcss, loginimagecss

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('', signupcss, name='css'),
    path('', loginimagecss, name='loginimage')
]

