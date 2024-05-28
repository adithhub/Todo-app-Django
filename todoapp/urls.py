from django.urls import path
from . import views

urlpatterns = [
    path('',views.task_view,name="task_view"),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
]