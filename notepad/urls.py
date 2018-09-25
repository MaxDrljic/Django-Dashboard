from django.urls import path

from .views import create_view, list_view, delete_view, update_view

app_name = 'notes'

urlpatterns = [
    path('create/', create_view, name='create'),
    path('list/', list_view, name='list'),
    path('<slug:id>/delete/', delete_view, name='delete'),
    path('<slug:id>/update/', update_view, name='update')
]
