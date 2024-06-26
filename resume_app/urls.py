
"""
URL configuration for resume_uploader project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views


from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',views.login_request,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout_view,name="logout"),
    path('profile',views.profile,name="profile"),
    
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
        
    path('uploads',views.send_files,name="uploads"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('resume',views.resume,name="resume"),
    path('delete-resume/<int:id>',views.delete_resume,name="delete-resume"),
    path('edit-resume/<int:id>',views.edit_resume,name="edit-resume"),
    path('update-resume/<int:id>',views.update_resume,name="update-resume"),


    path('roles',views.roles,name="roles"),
    path('location',views.location,name="location"),
    path('company',views.company,name="company"),
    path('employees',views.employee,name="employees"),
    
    path('add-roles',views.add_roles,name="add-roles"),
    path('edit-roles/<int:id>',views.edit_roles,name="edit-roles"),
    path('update-roles/<int:id>',views.update_roles,name="update-roles"),
    path('delete-roles/<int:id>',views.delete_role,name="delete-roles"),
    path('add-location',views.add_location,name="add-location"),
    path('edit-location/<int:id>',views.edit_location,name="edit-location"),
    path('update-location/<int:id>',views.update_location,name="update-location"),
    path('delete-location/<int:id>',views.delete_location,name='delete-location'),
    path('add-company',views.add_company,name="add-company"),
    path('edit-company/<int:id>',views.edit_company,name="edit-company"),
    path('delete-company/<int:id>',views.delete_company,name="delete-company"),
    path('update-company/<int:id>',views.update_company,name="update-company"),
    path('add-resume',views.add_resume,name="add-resume"),
    path('role-status/<int:id>',views.role_status,name="role-status"),
    path('location-status/<int:id>',views.location_status,name="location-status"),
    path('company-status/<int:id>',views.company_status,name="company-status"),    
    path('index',views.index,name="index"),

     

]
