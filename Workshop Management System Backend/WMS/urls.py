from django.urls import path
from .views import registration, login, admin_dashboard, organizer_dashboard, techinician_dashboard, edit_task, postpone_task, undo_task, delete_task, delete_user, logout

urlpatterns = [
    path('registration/', registration, name='Registration'),
    path('login/', login, name='Login'),
    path('admin_dashboard/', admin_dashboard, name='Admin_Dashboard'),
    path('organizer_dashboard', organizer_dashboard, name='Organizer_Dashboard'),
    path('technician/', techinician_dashboard, name="Technician_Dashboard" ),
    path('postpone-task/<int:task_id>/', postpone_task, name='Postpone_Task'),
    path('edit_task/<int:task_id>/', edit_task, name='Edit_Task'),
    path('undo_task/<int:task_id>/', undo_task, name='Undo_Task'),
    path('delete_task/<int:task_id>/', delete_task, name='Delete_Task'),
    path('delete_user/<int:user_id>/', delete_user, name='Delete_User'),
    path('logout/', logout, name='Logout'),
]
