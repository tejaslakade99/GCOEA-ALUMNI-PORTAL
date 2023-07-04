from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save
from django.dispatch import receiver

def user_directory_path_for_admin(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    obj = instance.first_name+'_'+instance.last_name
    filename = filename.split('.')[-1]
    return 'Hod/Thumbnails/user_{0}/{1}'.format(obj, 'thumbnail.' + filename)


def user_directory_path_for_faculty(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    obj = instance.first_name+'_'+instance.last_name
    filename = filename.split('.')[-1]
    return 'Faculty/Thumbnails/user_{0}/{1}'.format(obj, 'thumbnail.' + filename)


def user_directory_path_for_alumni(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    obj = instance.first_name+'_'+instance.last_name
    filename = filename.split('.')[-1]
    return 'Alumni/Thumbnails/user_{0}/{1}'.format(obj, 'thumbnail.' + filename)


def user_directory_path_for_students(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        obj = instance.first_name+'_'+instance.last_name
        filename = filename.split('.')[-1]
        return 'Students/Thumbnails/user_{0}/{1}'.format(obj, 'thumbnail.' + filename)
# # Create your models here.


class Role(models.TextChoices):
    ADMIN = "HOD", 'Hod'
    FACULTY = "FACULTY", 'Faculty'
    ALUMNI = "ALUMNI", 'Alumni'
    STUDENT = "STUDENT", 'Student'
class Branch(models.TextChoices):
    CS = "CS", 'Computer Science'
    IT = "IT", 'Information Technology'
    ENTC = "ENTC", 'Electronics and Telecommunication'


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    # role = models.CharField(max_length=50,choices=Role.choices)
    branch = models.CharField(max_length=50, choices=Branch.choices)
    roll_id = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to=user_directory_path_for_students)

class AlumniProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='alumni_profile')
    # role = models.CharField(max_length=50, choices=Role.choices)
    branch = models.CharField(max_length=50, choices=Branch.choices)
    roll_id = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to=user_directory_path_for_alumni)
    github_url = models.URLField(max_length=200)
    linkedin_url = models.URLField(max_length=200)
    portfolio_url = models.URLField(max_length=200)

class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty_profile')
    # role = models.CharField(max_length=50, choices=Role.choices)
    branch = models.CharField(max_length=50, choices=Branch.choices)
    # faculty_id = models.AutoField()
    profile_pic = models.ImageField(upload_to=user_directory_path_for_faculty)
    designation = models.CharField(max_length=200)
    linkedin_url = models.URLField(max_length=200)
    reasearch_gate_url = models.URLField(max_length=200)

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    branch = models.CharField(max_length=50, choices=Branch.choices)
    profile_pic = models.ImageField(upload_to=user_directory_path_for_admin)
    designation = models.CharField(max_length=200)
    linkedin_url = models.URLField(max_length=200)
    reasearch_gate_url = models.URLField(max_length=200)