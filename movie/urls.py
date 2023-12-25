from django.urls import path
from .views import movie_list, movie_detail, movie_create, movie_delete, movie_edit

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('<int:pk>/', movie_detail, name='movie_detail'),
    path('create/', movie_create, name='movie_create'),
    path('<int:pk>/edit/', movie_edit, name='movie_edit'),
    path('<int:pk>/delete/', movie_delete, name='movie_delete')

    # Add other URL patterns as needed
]
