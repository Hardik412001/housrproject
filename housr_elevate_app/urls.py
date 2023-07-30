from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import Resident_all_listing , Homepage
from django.views.generic import TemplateView


app_name = 'housr_elevate_app'

urlpatterns = [
    path('Resident_all_listing/', Resident_all_listing, name='Resident_all_listing'),
    path('housr_elevate_home/', Homepage, name='housr_elevate_home'),
]