from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Users Model: Represents user information
class Users(models.Model):
    # Fields for user information
    username = models.CharField(max_length=100, null=False)  # User's username
    contacts = PhoneNumberField()  # User's phone number
    email = models.EmailField(max_length=255, null=True)  # User's email address
    password = models.CharField(max_length=255, null=False)  # Hashed password
    role = models.CharField(max_length=20, null=False)  # User's role (e.g., Administrator, Organizer)
    date_created = models.DateTimeField(default=timezone.now)


    class Meta:
        app_label = 'WMS'  # App label for the model
    def __str__(self):
        return self.username  # Human-readable representation of the model instance

# Tasks Model: Represents tasks and their details
class Tasks(models.Model):
    # Fields for task details
    category = models.CharField(max_length=100, null=False)  # Task category
    device = models.CharField(max_length=100, null=False)  # Device associated with the task
    task = models.CharField(max_length=255, null=False)  # Task description
    status = models.CharField(max_length=50, null=False)  # Task status (e.g., On Pending, Completed)
    deadline = models.DateField()  # Deadline for the task
    technician_assigned = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        app_label = 'WMS'
