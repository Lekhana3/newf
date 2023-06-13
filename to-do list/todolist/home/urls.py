from django.urls import path,include
from . import views
from home import views
from django.contrib import admin


admin.site.site_header="login to Developer Lekhana"
admin.site.index_title="welcome to this portal"
urlpatterns = [
    path('home',views.home,name="home"),
    path('',views.home,name="home"),
    path('tasks',views.tasks,name="tasks"),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
   
]