from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse
from employee_information.models import Department, Position, Employees,Project
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json
from employee_information.models import Employees
from employee_information.views import team_details
from .forms import UploadFileForm
from leadview.models import files1
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


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
def home_lead(request):
    pid=request.user
    data=(Employees.objects.filter(code=pid).values)
    dept=Employees.objects.get(code=pid).department_id
    pos=Employees.objects.get(code=pid).position_id
    proj=Employees.objects.get(code=pid).project_id
    c=Employees.objects.get(code=pid).project_id.pk
    print(c)
    count=Employees.objects.filter(project_id_id=c).count()
    print(count)

    team_members=Employees.objects.filter(project_id_id=c)
    print(team_members)
    d=data
    print(d)
    
    
    context={
       'data':data,
       'dept':dept,
       'pos':pos,
       'proj':proj,
       'count':count,
       'team_members':team_members,
   }
    print(data)
    
    return render(request,'lead_view/home_lead.html',context)



def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        name2=request.POST.get('name1')
        pid=request.user
        c=Employees.objects.get(code=pid).project_id.name
        file_list=files1.objects.filter(project_id1=c)

        print(files)
        print(name2)
        print(form.is_valid())
        print(form.errors)
        pid=request.user
        #resp={'status':'success'}
        a=Employees.objects.get(code=pid).project_id
        if form.is_valid():
            print("entered")
            for f in files:
                #handle_uploaded_file(f)
                store=files1(project_id1=a,name=name2,file_uploaded=f)
                print(store)
                print("we did it")
                store.save()
            
            context = {'msg' : '<span style="color: green;">File successfully uploaded</span>','file_list':file_list}
            print("yes saved")
           
            return render(request, "lead_view/file_upload.html", context)
    else:
        form = UploadFileForm()
   
    pid=request.user
    c=Employees.objects.get(code=pid).project_id.name
    file_list=files1.objects.filter(project_id1=c)

    context={
      'file_list':file_list,
      'form':form
    }
    #print(file_list)
    return render(request, 'lead_view/file_upload.html', context)

def delete(request, id):
  member = files1.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('file-upload'))
