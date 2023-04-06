from django.shortcuts import redirect, render
from django.http import HttpResponse
from employee_information.models import Department, Position, Employees,Project,notification
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json
from employee_information.models import Employees,Project
from leadview.models import files1
from .forms import LeaveCreationForm
from django.contrib import messages


employees = [

    {
        'code':1,
        'name':"John D Smith",
        'contact':'09123456789',
        'address':'Sample Address only'
    },{
        'code':2,
        'name':"Claire C Blake",
        'contact':'09456123789',
        'address':'Sample Address2 only'
    }
]

def notices_emp(request):
    context={
        'notices':notification.objects.order_by('-time')
    }
    return render(request,'employee_view/notices.html',context)

def home_employee(request):
    context = {
        'page_title':'Home',
        'employees':employees,
        'total_department':len(Department.objects.all()),
        'total_position':len(Position.objects.all()),
        'total_employee':len(Employees.objects.all()),
    }
    return render(request, 'employee_view/home_employee.html',context)

def current_project(request):
    pid=request.user
    print(pid)

    c=Employees.objects.get(code=pid).project_id.name
    print(c)
    proj=Project.objects.filter(name=c)
    print(proj)
    file_list=files1.objects.filter(project_id1=c)
    print(file_list)
    print(files1.objects.all())
    context={
        'file_list':file_list,
        'proj':proj,

    }                           
    return render(request,'employee_view/current_project.html',context)

def leave_request(request):
    form=LeaveCreationForm(data=request.POST)
    if request.method=='POST':
        form=LeaveCreationForm(data=request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            user=request.user
            instance.user=user
            instance.save()
            messages.success(request,'Leave Request Sent,wait for ATA Freight Managers response',extra_tags = 'alert alert-success alert-dismissible show')
            return render(request,'employee_view/leave_request.html')
        messages.error(request,'failed to Request a Leave,please check entry dates',extra_tags = 'alert alert-warning alert-dismissible show')
    return render(request,'employee_view/leave_request.html',{'form':form})