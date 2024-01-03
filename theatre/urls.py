# myapp/urls.py
from django.urls import path
from .views import add_theatre, all_theatres, edit_theatre, view_theatre, delete_theatre

urlpatterns = [
    # ... other URL patterns
    path('', all_theatres, name='all_theatres'),
    path('add/', add_theatre, name='add_theatre'),
    path('edit/<int:theatre_id>/', edit_theatre, name='edit_theatre'),
    path('view/<int:theatre_id>/', view_theatre, name='view_theatre'),
    path('delete/<int:theatre_id>/', delete_theatre, name='delete_theatre'),


    
]
