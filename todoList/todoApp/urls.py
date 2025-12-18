from django.urls import path
from .views import todo_list, complete,delete,edit

urlpatterns=[
    path('',todo_list,name='todo_list'),
    path('complete/<int:todo_id>/',complete,name='complete'),
    path('delete/<int:todo_id>/',delete,name='delete'),
    path('edit/<int:todo_id>/',edit,name='edit'),  
]