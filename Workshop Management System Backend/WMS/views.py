from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Users, Tasks

def registration(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve user data from the registration form
        username = request.POST['username'].lower()
        contacts = request.POST['contacts']
        email = request.POST['email'].lower()
        password = request.POST['password']
        
        # Hash the provided password
        hashed_password = make_password(password)

        # Create a new user instance and save it to the database
        new_user = Users(username=username, contacts=contacts, email=email, password=hashed_password)
        new_user.save()
        
        # Check if user registration was successful and redirect to login page
        if new_user.id is not None:
            return redirect('Login')
    
    # If not a POST request, render the registration page
    return render(request, 'registration.html')


# Login View
def login(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve username and password from the form
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        # Find the user by their username
        user = Users.objects.filter(username=username).first()
        
        # Check the provided password against the user's stored password
        checked_password = check_password(password, user.password)
        
        if user:
            if checked_password:
                # Redirect based on the user's role
                if user.role == "Administrator":
                    response = redirect('Admin_Dashboard')
                    response.set_cookie('username', user.username.title(), max_age=604800)
                    response.set_cookie('role', 'admin', max_age=604800)
                    return response
                
                elif user.role == "Organizer":
                    response = redirect('Organizer_Dashboard')
                    response.set_cookie('username', user.username.title(), max_age=604800)
                    response.set_cookie('role', 'organizer', max_age=604800)
                    return response
                
                elif user.role == "Technician":
                    response = redirect('Technician_Dashboard')
                    response.set_cookie('username', user.username.title(), max_age=604800)
                    response.set_cookie('role', 'technician', max_age=604800)
                    response.set_cookie('id', user.id, max_age=604800)
                    return response
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'login.html')
        
        else:
            messages.error(request, 'User not found')
            return render(request, 'login.html')
    
    # If not a POST request, render the login page
    return render(request, 'login.html')

# Admin's view
def admin_dashboard(request):
    
    total_technician = Users.objects.filter(role='Technician').count()
    total_organizer = Users.objects.filter(role='Organizer').count()
    total_users = total_organizer + total_technician
    
    total_task = Tasks.objects.all().count()
    
    # Retrieve the username from cookies
    username = request.COOKIES.get('username')
    
    # Check if the user is logged in
    if request.COOKIES.get('role') != 'admin':
        messages.error(request, 'Please log in first to access the dashboard')
        return redirect('Login')
    
    else:
        # Prepare context for rendering the template
        context = {
            'total_technician': total_technician,
            'total_organizer': total_organizer,
            'total_users': total_users,
            'total_task': total_task,
            'username': username
        }
        return render(request, 'admin_dashboard.html', context)

    

# Organizer's view    
def organizer_dashboard(request):
    # Retrieve the username from cookies
    username = request.COOKIES.get('username')
    
    # Check if the user is logged in
    if request.COOKIES.get('role') != 'organizer':
        messages.error(request, 'Please log in first to access the dashboard')
        return redirect('Login')    
    
    else:
        # Handle form submission
        if request.method == 'POST':
            # Retrieve form data
            category = request.POST['category'].title()
            device = request.POST['device'].title()
            task = request.POST['task'].title()
            date = request.POST['deadline']
            technician_assigned = request.POST['technician']
            
            # Fetch technician details
            technician = Users.objects.get(username=technician_assigned)
            
            # Create a new task instance
            new_task = Tasks(category=category, device=device, task=task, status="Pending", deadline=date, technician_assigned=technician)
            new_task.save()
            
            return redirect('Organizer_Dashboard')
            
        # Fetch list of technicians
        technicians = Users.objects.filter(role='Technician')
        formatted_technicians = [technician_list.username.title() for technician_list in technicians]
        
        # Fetch total task count and all tasks
        total_task = Tasks.objects.count()
        tasks = Tasks.objects.all()
        tasks = Tasks.objects.all().order_by('-date_created')
        
        paginator = Paginator(tasks, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # Fetch total users count and all users
        users = Users.objects.filter(role='Technician')
        total_technicians = users.count()
        
        # Fetch total users count and all users
        tasks_done = Users.objects.filter(role='Done').count()
        tasks_pending = Tasks.objects.filter(status='Pending').count()

        # Prepare context for rendering the template
        context = {
            'username': username,
            'technicians_list': formatted_technicians,
            'total_task': total_task,
            # 'tasks': tasks,
            'total_users': total_technicians,
            'tasks_done': tasks_done,
            'tasks_pending': tasks_pending,
            'users': users,
            'tasks_paginator': page_obj
        }
        return render(request, 'Organizer.html', context)
    
# Technician's view    
def techinician_dashboard(request):
    # Retrieve the username from cookies
    username = request.COOKIES.get('username')
    
    # Check if the user is logged in
    if request.COOKIES.get('role') != 'technician':
        messages.error(request, 'Please log in first to access the dashboard')
        return redirect('Login')    
    
    else:   
        user_id = request.COOKIES.get('id')
        user = Users.objects.get(id=user_id)
        
        # Fetch total task count and all tasks
        total_task = Tasks.objects.filter(technician_assigned=user_id).count()
        tasks = Tasks.objects.filter(technician_assigned=user_id).order_by('-date_created')
        # tasks = Tasks.objects.all().order_by('-date_created')
        
        paginator = Paginator(tasks, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # # Fetch total users count and all users
        # tasks_done = Users.objects.filter(id=user_id, role='Done').count()
        # tasks_pending = Tasks.objects.filter(id=user_id, status='Pending').count()

        # Prepare context for rendering the template
        context = {
            'username': username,
            'total_task': total_task,
            # 'tasks_done': tasks_done,
            # 'tasks_pending': tasks_pending,
            'tasks_paginator': page_obj
        }
        return render(request, 'technician.html', context)
    

# What happens when organizer clicks postpone button    
def postpone_task(request, task_id):
    try:
        task_to_postpone = Tasks.objects.get(pk=task_id)
        task_to_postpone.status = 'Postponed'
        task_to_postpone.save()
    except Tasks.DoesNotExist:
        pass
    return redirect('Organizer_Dashboard')

# What happens when organizer clicks undo button    
def undo_task(request, task_id):
    try:
        task_to_postpone = Tasks.objects.get(pk=task_id)
        task_to_postpone.status = 'Pending'
        task_to_postpone.save()
    except Tasks.DoesNotExist:
        pass
    return redirect('Organizer_Dashboard')

def delete_task(request, task_id):
    try:
        task_to_postpone = Tasks.objects.get(pk=task_id)
        task_to_postpone.delete()
    except Tasks.DoesNotExist:
        pass
    return redirect('Organizer_Dashboard')

# What happens when organizer clicks edit button
def edit_task(request, task_id):
    try:
        task_to_edit = Tasks.objects.get(pk=task_id)
    
    except Tasks.DoesNotExist:
        pass
    
def delete_user(request, user_id):
    try:
        user_to_delete = Users.objects.get(pk=user_id)
        user_to_delete.delete()
    except Tasks.DoesNotExist:
        pass
    return redirect('Organizer_Dashboard')

# View for logging out   
def logout(request):
    
    response = render(request, 'logout.html')
    response.delete_cookie('sessionid')
    response.delete_cookie('admin')
    response.delete_cookie('organizer')
    response.delete_cookie('username')
    
    return response