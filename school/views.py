from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexPage(TemplateView):
    template_name = 'index.html'    

class StaffPage(TemplateView):
    template_name = 'staff.html'

class SportsPage(TemplateView):
    template_name = 'sports.html'

class AdmissionsPage(TemplateView):
    template_name = 'admissions.html'

class CalendarPage(TemplateView):
    template_name = 'calendar.html'
