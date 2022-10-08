from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static
from .views import IndexPage, StaffPage, SportsPage, AdmissionsPage

urlpatterns = [
    path('', views.IndexPage.as_view(),name='index'),
    path('staff', views.StaffPage.as_view(),name='staff'),
    path('sports', views.SportsPage.as_view(),name='sports'),
    path('admissions', views.AdmissionsPage.as_view(),name='admissions'),
    path('calendar', views.CalendarPage.as_view(),name='calendar'),
]
