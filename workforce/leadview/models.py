from django.db import models
from django.utils.timezone import now


# Create your models here.
class files1(models.Model):
    project_id1=models.CharField(max_length=255)
    name=models.CharField(max_length=255,default='demo file',blank=True,null=True)
    file_uploaded=models.FileField(upload_to='media')
    date= models.DateField(blank=True,default=now)

    #def __str__(self):
		#return self.firstname