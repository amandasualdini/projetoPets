from django.urls import path
from .views import list_petEncontrado, create_petEncontrado, update_petEncontrado, delete_petEncontrado

urlpatterns = [
    path('', list_petEncontrado, name='list_petEncontrado'),
    path('new', create_petEncontrado, name='create_petEncontrado'),
    path('update/<int:id>/', update_petEncontrado, name='update_petEncontrado'),
    path('delete/<int:id>/', delete_petEncontrado, name='delete_petEncontrado'),
]