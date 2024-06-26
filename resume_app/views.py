from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth import login as auth_login
# from django.contrib.auth.forms import NewLoginForm
from django.contrib.auth.forms import AuthenticationForm 
from .forms import NewUserForm
from django.contrib import messages
from .models import *
from django.contrib.auth import logout
import os
import fitz
from django.http import JsonResponse
from .documents import myuploadfileDocument
from elasticsearch_dsl.query import MultiMatch

# Create your views here.
def login_request(request): 
  if request.method=="POST":
    print("Form was submitted")
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      print(form.is_valid())
      username = form.request.POST.get('username')  
      password = form.request.POST.get('password')
      user = authenticate(username=username, password=password)
      # user=form.save()
      if user:
        login(request,user)
        messages.success(request,"login successful")
        print("asddas")
        return redirect("dashboard")
      
    for error in form.non_field_errors():
      messages.error(request, error)
      print(form.errors)
    return redirect("login")        
     
  else:
    form=AuthenticationForm()
  return render(request,'login.html',context={"login_form":form})

def register(request):
  if request.method=="POST":
    form=NewUserForm(request.POST)
    if form.is_valid():
      user=form.save()
      print("form saved")
      messages.success(request,"registration Successful")
      return redirect("/")
    messages.error(request,"Unsuccessful")      
  else:
   form=NewUserForm()
  return render(request,'register.html',context={"register_form":form})


def logout_view(request):
    logout(request)
    return redirect('login')


def profile(request):
  roles=Roles.objects.all()
  location=Location.objects.all()
  company=Company.objects.all()
  return render(request,'profile.html',{'roles':roles,'location':location,'company':company})


# def send_files(request):
  
#   if request.method=="POST":
#     try:
            
#       role=request.POST['role']
#       location=request.POST['location']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
#       company=request.POST['company']

#       myfile=request.FILES.getlist('uploadfiles[]')

#       if not role:
#         messages.error(request, "Please Enter Role")

#       if not location: 
#         messages.error(request, "Please Enter Location")
    
#       if not myfile:
#         messages.error(request,"Please Upload the resume")
    
#       error_messages = list(messages.get_messages(request))
#       if error_messages:
#         print(error_messages)
#         return redirect('add-resume')

#       for f in myfile:
#         directory_name = role  
#         file_path = handle_uploaded_file(f, directory_name)
#         with open(file_path, 'wb+') as destination:
#            for chunk in f.chunks():
#              destination.write(chunk)        
#         username=request.user.username
#         myuploadfile(role_name=role,location=location,company_name=company,myfiles=file_path,created_by=username).save()
    
#     except Exception as e:  
#       messages.error(request, "An error occurred while processing your request.")
#       print("Exception occurred:", e)
#       return redirect('add-resume')
    
#     messages.success(request, "Resume Uploaded Successfully!")
#     return redirect('resume')
  
  

def handle_uploaded_file(f,directory_name):
  new_dir_path_recursive = f'resume_files/{directory_name}'
  os.makedirs(new_dir_path_recursive, exist_ok=True)
  file_path=os.path.join('resume_files',directory_name,f.name)
  with open(file_path, 'wb+') as destination:
    for chunk in f.chunks():
      destination.write(chunk)
  return file_path


def dashboard(request):
  return render(request,"dashboard.html")
  
def resume(request):  
  resume_data=myuploadfile.objects.filter(is_Delete=False)  
  return render(request,"resume.html",{"resume_data":resume_data})

def roles(request):
  role=addRoles.objects.filter(is_Delete=False).order_by('-created_at')
  return render(request,"roles.html",{'role':role})

def location(request):
  location=addLocation.objects.filter(is_Delete=False).order_by('-created_at')
  return render(request,"location.html",{"location":location})  

def company(request):
  company=addCompany.objects.filter(is_Delete=False).order_by('-created_at')
  # company=addCompany.objects.filter(is_Delete=False).order_by('-created_at')
  return render(request,"company.html",{"company":company})

def employee(request):
  return render(request,"employee.html")

def add_roles(request):
  if request.method=="POST":
    try:
      response={}
      role=request.POST['role']
      if not role:
        messages.error(request, "Please Enter Role")
      
      if addRoles.objects.filter(role_name=role).exists():
        messages.error(request, "Role Already Exists")
        return redirect('add-roles')      
    
    except Exception as e:  
      messages.error(request, "An error occurred while processing your request.")
      print("Exception occurred:", e)
      return redirect('add-roles')
    
    username=request.user.username
    print(username)
    addRoles(role_name=role,created_by=username).save()
    messages.success(request, "Role added successfully!")
    return redirect('roles')    
  
  return render(request,"role_form.html",{'edit_mode':False})


def edit_roles(request,id):  
  if request.method=="POST":    
    role=request.POST['role']
    if not role:
      messages.error(request, "Please Enter Role")
      return redirect('edit-roles')  
      
    if addRoles.objects.filter(role_name=role).exists():
      messages.error(request, "Role Already Exists")
      return redirect('edit-roles') 
    
  instance=addRoles.objects.get(id=id)
  return render(request,'role_form.html',{'instance':instance,'edit_mode':True})

def update_roles(request,id):
  instance=addRoles.objects.get(id=id)
  if request.method=="POST":
    role=request.POST['role']

    if not role:
      messages.error(request, "Please Enter Role")
      return redirect('edit-roles')  
      
    if addRoles.objects.filter(role_name=role).exclude(id=id).exists():
      messages.error(request, "Role Already Exists")
      return redirect('edit-roles',id=id)  
    try:
      username=request.user.username
      instance.role_name=role
      instance.created_by = username
      instance.save()  
      messages.success(request, "Role updated successfully!")
      return redirect("/roles")
    except Exception as e:
      messages.error(request, "An error occurred while processing your request.")
      print("Exception occurred:", e)
      return redirect('edit-roles')
  return render(request,'role_form.html',{'instance':instance,'edit_mode':True})  


def delete_role(request,id):
  data=addRoles.objects.get(id=id)
  data.is_Delete=True
  data.save()
  return redirect('roles')


def add_location(request):
  if request.method=="POST":
    try:
      location=request.POST['location']
      if not location:
        messages.error(request, "Please Enter Location")
      
      if addLocation.objects.filter(location_name=location).exists():
        messages.error(request, "Location Already Exists")
        return redirect('add-location')
      
    except Exception as e:  
      messages.error(request, "An error occurred while processing your request.")
      print("Exception occurred:", e)
      return redirect('add-location')
        
    username=request.user.username
    print(username)
    addLocation(location_name=location,created_by=username).save()
    messages.success(request, "Location added successfully!")
    return redirect('location')
  return render(request,"location_form.html",{'edit_mode': False})
 
def edit_location(request,id):
  instance=addLocation.objects.get(id=id)
  return render(request,'location_form.html',{'instance':instance,'edit_mode': True})  

def update_location(request,id):
  
  instance=addLocation.objects.get(id=id)
  if request.method=="POST":
    location=request.POST['location']
    if not location:
      messages.error(request,"Please Enter the Location")
    
    if addLocation.objects.filter(location_name=location).exclude(id=id).exists():
      messages.error(request, "Location Already Exists")
      return redirect('edit-location',id=id)  
    
    try:
      username=request.user.username
      instance.location_name=location
      instance.created_by = username
      instance.save()
      messages.success(request, "Location updated successfully!")
      return redirect("/location")
    
    except Exception as e:
      messages.error(request, "An error occurred while processing your request.")
      print("Exception occurred:", e)
      return redirect('edit-location')
  
  return render(request,'location_form.html',{instance:instance,'edit_mode':True})
  
def delete_location(request,id):
  data=addLocation.objects.get(id=id)
  data.is_Delete=True
  data.save()
  return redirect('location')

def add_company(request):
  if request.method=="POST":
    try:
      company=request.POST['company']
      if not company:
        messages.error(request,"Please Enter Company")
      
      if addCompany.objects.filter(company_name=company).exists():
        messages.error(request,"Company Already Exist")
        return redirect('add-company')  

    except Exception as e:
      messages.error(request, "An error occurred while processing your request.")
      print("Exception occurred:", e)
      return redirect('add-company')  
    username=request.user.username
    print(username)
    addCompany(company_name=company,created_by=username).save()  
    messages.success(request, "Company added successfully!")
    return redirect('company')  
  
  return render(request,"company_form.html",{'edit_mode': False})


def edit_company(request, id):
  instance=addCompany.objects.get(id=id)
  return render(request, 'company_form.html', {'instance': instance, 'edit_mode': True})


def update_company(request, id):
  instance=addCompany.objects.get(id=id)
  if request.method=="POST":
    company=request.POST['company']
    if not company:
        messages.error(request,"Please Enter Company")
    
    if addCompany.objects.filter(company_name=company).exclude(id=id).exists():
      messages.error(request, "Company Already Exists")
      return redirect('edit-company',id=id) 
    
    try:
      username=request.user.username
      print(username)
      instance.company_name = company
      instance.created_by = username
      instance.save()
      messages.success(request, "Company updated successfully!")
      return redirect("/company")  
         
    except Exception as e:
      messages.error(request, "An error occurred while processing your request.")
      print("Exception occurred:", e)
      return redirect('edit-company')

  return render(request, 'company_form.html', {'instance': instance,'edit_mode': True})  


def delete_company(request,id):
  
  data=addCompany.objects.get(id=id)
  data.is_Delete=True
  data.save()
  return redirect('company')


def add_resume(request):
  roles=addRoles.objects.filter(is_Delete=False)
  location=addLocation.objects.filter(is_Delete=False)
  company=addCompany.objects.filter(is_Delete=False)
  return render(request,'add-resume.html',{"roles":roles,"location":location,"company":company})


def role_status(request,id):
  data=addRoles.objects.get(id=id)
  if data.status==False:
    data.status=True
  else:
    data.status=False
  data.save()
  print("Data",data)
  return redirect('roles')  


def location_status(request,id):
  data=addLocation.objects.get(id=id)
  if data.status==False:
    data.status=True
  else:
    data.status=False
  data.save()
  return redirect('location')


def company_status(request,id):
  data=addCompany.objects.get(id=id)
  if data.status==False:
    data.status=True
  else:
    data.status=False
  data.save()
  return redirect('company')
  

def delete_resume(request,id):
  
  data=myuploadfile.objects.get(id=id)
  print("data")
  print(data)
  if data.is_Delete == False:
    data.is_Delete=True
  else:
    data.is_Delete=False
  data.save()
  return redirect("resume")


# def edit_resume(request,id):
#   instance=myuploadfile.objects.get(id=id)
#   return render(request,"add-resume.html",{'instance':instance,"edit_mode":True})

def edit_resume(request,id):
    instance = myuploadfile.objects.get(id=id)  
    roles = addRoles.objects.filter(is_Delete=False)
    location = addLocation.objects.filter(is_Delete=False)
    company = addCompany.objects.filter(is_Delete=False)
    return render(request, "add-resume.html", {'instance': instance, "edit_mode": True, "roles": roles, "location": location, "company": company})


def update_resume(request,id):
    
  instance=myuploadfile.objects.get(id=id)
  roles=addRoles.objects.filter(is_Delete=False)
  location=addLocation.objects.filter(is_Delete=False)
  company=addCompany.objects.filter(is_Delete=False)
  
  if request.method=="POST":
    roles=request.POST['role']
    print(roles)
    
    location=request.POST['location']
    print(location)
    
    company=request.POST['company']
    print(company)
        
    if not roles:
      messages.error(request,"Please Enter Roles")
      return redirect('resume')
    
    if not location:
      messages.error(request,"Please Enter Location")
      return redirect('resume')

    # if not company:
    #   messages.error(request,"Please Enter Company")
    #   return redirect('resume')
    
    try:                        
      username=request.user.username
      # instance.role_name = roles
      # instance.company_name = company
      # instance.location = location
      # instance.created_by = username
      instance.save()
      messages.success(request, "Resume updated successfully!")
      return redirect("/resume")  
         
    except Exception as e:
      messages.error(request, "An error occurred while processing your request.")
      print("Exception occurred:", e)
      return redirect("edit-resume", id=id)
  
  return render(request, "add-resume.html", {'instance': instance, "edit_mode": True, "roles": roles, "location": location, "company": company})







    

def extract_text_from_pdf(file_path):
  print("file_path",file_path)
  if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: '{file_path}'")
      
  doc=fitz.open(file_path)
  text=""
  
  for page_num in range(len(doc)):
    page=doc.load_page(page_num)
    text+=page.get_text()
    
  doc.close()
  
  return text



def send_files(request):
    if request.method == "POST":
        try:
            role = request.POST.get('role')
            location = request.POST.get('location')
            company = request.POST.get('company')
            myfile = request.FILES.getlist('uploadfiles[]')

            # Validate inputs
            if not role:
                messages.error(request, "Please Enter Role")
            if not location:
                messages.error(request, "Please Enter Location")
            if not myfile:
                messages.error(request, "Please Upload the resume")

            error_messages = list(messages.get_messages(request))
            if error_messages:
                print(error_messages)
                return redirect('add-resume')

            # Process each uploaded file
            for f in myfile:
                directory_name = role  
                file_path = handle_uploaded_file(f, directory_name)
                print("file_path",file_path)

                # Extract text from the PDF
                extracted_text = extract_text_from_pdf(file_path)
                print("extracted_text",extracted_text)

                # Save the uploaded file information
                username = request.user.username
                my_uploaded_file = myuploadfile(
                    role_name=role,
                    location=location,
                    company_name=company,
                    myfiles=file_path,
                    created_by=username,
                    extracted_text=extracted_text 
                )
                my_uploaded_file.save()

        except Exception as e:
            messages.error(request, "An error occurred while processing your request.")
            print("Exception occurred:", e)
            return redirect('add-resume')

        messages.success(request, "Resume Uploaded Successfully!")
        return redirect('resume')



def index(request):
  context={}
  q=request.GET.get("q")
  # print("Request GET data:", request.GET)  
  print("Search term:", q)  
  if q:
    
    # old procedure not working
    # s=myuploadfileDocument.search().query("match",extracted_text="q")
    # print("s",s)
    # response = s.execute()  
    # print("Elasticsearch response:", response.to_dict()) 
    # resumes = response.hits   
    # print("resume,",resumes)  
         
    # context = {
    #     "resumes": resume
    # }
        
    # new procedure working
    query = MultiMatch(query=q, fields=["extracted_text"], fuzziness="AUTO")
    print("query",query)
    s = myuploadfileDocument.search().query(query)
    response = s.execute()
    # context["resumes"] = s
    resumes = [
            {
                "file_url": hit.myfiles,
                "role_name": hit.role_name,
                "location": hit.location,
                "extracted_text":hit.extracted_text,
                "company_name": hit.company_name
            }
            for hit in response
        ]
    context["resumes"] = resumes
  return render(request,"resume.html",context)
