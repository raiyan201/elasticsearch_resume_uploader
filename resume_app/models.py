from django.db import models
from django.utils import timezone

# Create your models here.
class Roles(models.Model):
    role_name=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.role_name
    
class Location(models.Model):
    location=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.location

class Company(models.Model):
    company_name=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.company_name


class myuploadfile(models.Model):

    role_name =models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    company_name=models.CharField(max_length=100,null=True,blank=True)
    f_name=models.CharField(max_length=200,default="default_name")
    status=models.BooleanField(default=True)
    myfiles=models.FileField(upload_to="")
    created_at = models.DateTimeField(default=timezone.now)
    created_by=models.CharField(max_length=200,blank=True,null=True)
    is_Delete=models.BooleanField(default=False)
    extracted_text = models.TextField(default='')
    
    
    def __str__(self):
      return self.role_name


class addRoles(models.Model):
    role_name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(max_length=200,blank=True,null=True)
    is_Delete=models.BooleanField(default=False)

    def __str__(self):
        return self.role_name
    
class addLocation(models.Model):
    location_name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(max_length=200,blank=True,null=True)
    is_Delete=models.BooleanField(default=False)

    def __str__(self):
        return self.location_name
    
class addCompany(models.Model):
    company_name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(max_length=200,blank=True,null=True)
    is_Delete=models.BooleanField(default=False)
    def __str__(self):
        return self.company_name
    