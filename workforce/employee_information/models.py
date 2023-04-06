from datetime import datetime
from django.db import models
from django.utils import timezone
from django.utils.timezone import now


# Create your models here.
class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


class Project(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    completion=models.IntegerField()
    project_lead=models.CharField(max_length=100)
    start_date=models.DateTimeField(default=timezone.now)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
    files=models.FileField(null=True,blank=True,upload_to='media')

    def __str__(self):
        return self.name

    def datestarted(self):
        return self.start_date.strftime('%B %d %Y')
    



#EMPLOYEE_TYPE=(
    #('Employee','Employee'),
    #('Team Lead','Team Lead'),
    #('Fresher','Fresher')
    #)
class Employees(models.Model):
    code = models.CharField(max_length=100,blank=True) 
    firstname = models.TextField() 
    middlename = models.TextField(blank=True,null= True) 
    lastname = models.TextField() 
    gender = models.TextField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.EmailField()
    employeetype = models.TextField(default='Employee')
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    project_id=models.ForeignKey(Project, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField()
    lead=models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True)
    photo=models.ImageField(null=True, blank=True ,upload_to = 'photos')
    
    def __str__(self):
        return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '
    

class notification(models.Model):
    name=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.TextField(blank=True)
    time=models.DateTimeField(default=now)

class Task(models.Model):
    description=models.TextField()
    author=models.CharField(max_length=255)
    assigned=models.ForeignKey(Employees, on_delete=models.CASCADE)
    date= models.DateField(blank=True,default=now)