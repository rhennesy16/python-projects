from __future__ import unicode_literals
from django.db import models
import re
emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
nameRegex = re.compile(r'^[a-zA-Z ]+$')
passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

class LoginsManager(models.Manager):
    def basic_validator(self, postData):
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

class Logins(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = LoginsManager()
