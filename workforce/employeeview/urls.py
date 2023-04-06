from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView
from employeeview import views

urlpatterns = [
     path('home_employee', views.home_employee, name="home_employee"),
     #path('employee_dashboard/<int:pid>',views.employee_dashboard,name="employee_dashboard"),
     path('notices_emp',views.notices_emp,name="notices_emp"),
     path('current_project',views.current_project,name="current_project"),
     path('leave_request',views.leave_request,name="leave_request")
]