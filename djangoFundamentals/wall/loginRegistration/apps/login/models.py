from __future__ import unicode_literals
from django.db import models
import re, bcrypt
emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
nameRegex = re.compile(r'^[a-zA-Z ]+$')
passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

class UsersManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        # Check first name
        if len(postData['first_name']) < 0:
            errors['first_name'] = 'Please enter valid name'
        if not nameRegex.match(postData['first_name']):
            errors['first_name'] = "First name must be min 2 letters"
        # Check last name
        if len(postData['last_name']) < 0:
            errors['last_name'] = 'Please enter valid name'
        if not nameRegex.match(postData['last_name']):
            errors['last_name'] = "Last name must be min 2 letters"
        # Check email
        if len(postData['email']) < 7:
            errors['email'] = 'Email cannot be blank'
        if not emailRegex.match(postData['email']):
            errors['email'] = "Enter valid email"
        # Check password
        if len(postData['password']) < 7:
            errors['password'] = 'Password cannot be blank'
        if not passwordRegex.match(postData['password']):
            errors['password'] = "Password must contain at least one lowercase letter, one uppercase letter, and one digit"
        if postData['password']!=postData['confirm_password']:
            return redirect('/')
        return errors

    def login_validator(self, postData):
        user = Users.objects.filter(email=postData['email'])
        errors = {}
        if not user:
            errors['email'] = 'Please enter valid email or password.'
        if user and not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
            print(postData['password'])
            errors['password'] = 'Please enter valid email or password.'
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()

class Messages(models.Model):
    """docstring for Messages"""
    user = models.ForeignKey(Users, related_name="message")
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # comment
    
class Comments(models.Model):
    user = models.ForeignKey(Users, related_name="comment")
    message = models.ForeignKey(Messages, related_name="comment")
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)