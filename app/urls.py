from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('app/index.html', views.index, name = "index"),
    path('app/add-task.html', views.add_task, name = "add-task")
]