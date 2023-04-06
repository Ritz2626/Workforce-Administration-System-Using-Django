from django.shortcuts import redirect, render
from django.http import HttpResponse
from employee_information.models import Department, Position, Employees,Project,notification
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User


import json
team_members=""
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
# Login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':'',"type":'admin','link':"home-page",'type':'Employee'}
    username = ''
    password = ''
    type=''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None and username=='admin':
            if user.is_active:
                login(request, user)
                resp['status']='success'
                resp['type']='admin'
            else:
                resp['msg'] = "Incorrect username or password"
        elif user is not None:
             if user.is_active:
                login(request, user)
                resp['status']='success'
                resp['type']='employee'
                resp['link']=int(username)
                resp['type']=Employees.objects.get(code=username).employeetype
                print(resp['link'])
                print("yes")
                print(resp)
             else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')



#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')

# Create your views here.
@login_required
def home(request):
    context = {
        'page_title':'Home',
        'employees':employees,
        'total_department':len(Department.objects.all()),
        'total_position':len(Position.objects.all()),
        'total_employee':len(Employees.objects.all()),
    }
    return render(request, 'employee_information/home.html',context)


def about(request):
    context = {
        'page_title':'About',
    }
    return render(request, 'employee_information/about.html',context)

# Departments
@login_required
def departments(request):
    department_list = Department.objects.all()
    context = {
        'page_title':'Departments',
        'departments':department_list,
    }
    return render(request, 'employee_information/departments.html',context)
@login_required
def manage_departments(request):
    department = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            department = Department.objects.filter(id=id).first()
    
    context = {
        'department' : department
    }
    return render(request, 'employee_information/manage_department.html',context)

@login_required
def save_department(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_department = Department.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_department = Department(name=data['name'], description = data['description'],status = data['status'])
            save_department.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_department(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Department.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

# Positions
@login_required
def positions(request):
    position_list = Position.objects.all()
    context = {
        'page_title':'Positions',
        'positions':position_list,
    }
    return render(request, 'employee_information/positions.html',context)
@login_required
def manage_positions(request):
    position = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            position = Position.objects.filter(id=id).first()
    
    context = {
        'position' : position
    }
    return render(request, 'employee_information/manage_position.html',context)

@login_required
def save_position(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_position = Position.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],status = data['status'])
        else:
            save_position = Position(name=data['name'], description = data['description'],status = data['status'])
            print(save_position)
            save_position.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_position(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Position.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
# Employees
def employees(request):
    employee_list = Employees.objects.all()
    context = {
        'page_title':'Employees',
        'employees':employee_list,
    }
    return render(request, 'employee_information/employees.html',context)
@login_required
def manage_employees(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all()
    projects=Project.objects.all()
    print(projects) 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions,
        'projects':projects
    }
    return render(request, 'employee_information/manage_employee.html',context)

@login_required
def save_employee(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Employees.objects.exclude(id = data['id']).filter(code = data['code'])
    else:
        check  = Employees.objects.filter(code = data['code'])
    print(data['id'])
    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            dept = Department.objects.filter(id=data['department_id']).first()
            pos = Position.objects.filter(id=data['position_id']).first()
            proj= Project.objects.filter(id=data['project_id']).first()
            print('yes 1')
            print(data)
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_employee = Employees.objects.filter(id = data['id']).update(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],employeetype=data['employeetype'],department_id = dept,position_id = pos,project_id=proj,date_hired = data['date_hired'],salary = data['salary'],status = data['status'])
                print('yes 3')
            else:
                save_employee = Employees(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],employeetype=data['employeetype'],department_id = dept,position_id = pos,project_id=proj,date_hired = data['date_hired'],salary = data['salary'],status = data['status'])
                print("yes save")
                save_employee.save()
                user=User.objects.create_user(username=data['code'],password=data['email'])
                print(user)
                print('yes 2')
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(resp)
            print(save_employee)
            print(json.dumps({"code":data['code'], "firstname" : data['firstname'],"middlename" : data['middlename'],"lastname" : data['lastname'],"dob" : data['dob'],"gender" : data['gender'],"contact" : data['contact'],"email" : data['email'],"address" : data['address'],"employeetype":data['employeetype'],"department_id" : data['department_id'],"position_id" : data['position_id'],"project_id":data['project_id'],"date_hired" : data['date_hired'],"salary" : data['salary'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_employee(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Employees.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_employee(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    print(projects)
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions,
        
    }
    return render(request, 'employee_information/view_employee.html',context)

@login_required
# Employees
def projects(request):
    project_list = Project.objects.all()
    leads=Employees.objects.filter(lead=True)
    print(leads)
    context = {
        'page_title':'On-going Projects',
        'projects':project_list,
        'leads':leads,
    }
    return render(request, 'employee_information/projects.html',context)

@login_required
def view_project(request):
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(project_id=id)
    context = {
        'employee' : employee,
        
    }
    print(context)
    return render(request, 'employee_information/view_project.html',context)

def notifications(request):
    if request.method=="POST":
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        store=notification(name=name,subject=subject,message=message)
        store.save()
    return render(request,'employee_information/notifications.html')

@login_required
def employee_dashboard(request,pid):
    data=(Employees.objects.filter(code=pid).values)
    dept=Employees.objects.get(code=pid).department_id
    pos=Employees.objects.get(code=pid).position_id
    proj=Employees.objects.get(code=pid).project_id
    context={
       'data':data,
       'dept':dept,
       'pos':pos,
       'proj':proj
           
   }
    print(data)
    
    return render(request,'employee_view/home_employee.html',context)

@login_required
def teamlead_dashboard(request,pid):
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


def notices_emp(request):
    a=notification.objects.last()
    context={
        'notices':a
    }
    print(context['notices'])
    return render(request,'employee_view/notices.html',context)

print("yes 2-"+team_members)

@login_required
def team_details(request):
   user=request.user
   print(user.id)
   print(user)
   c=Employees.objects.get(code=user).project_id.pk
   team_members=Employees.objects.filter(project_id_id=c)
   context={
       'team_members':team_members
   }
   return render(request,'lead_view/team_details.html',context)

@login_required
def fresher_dashboard(request,pid):
    fresher=(Employees.objects.filter(code=pid).values)
    context={
        'fresher':fresher,
    }
    return render(request,'fresher_view/home_fresher.html',context)
