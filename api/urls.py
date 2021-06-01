
from django.urls import path
from api import views
app_name='api'

urlpatterns = [
    path('todo-list/',views.todo_view,name='todo list'),
    path('create/',views.todo_create,name='create'),
    path('one/<str:id>/',views.todo_one,name='one item'),
    path('update/<str:id>/',views.todo_update,name='update'),
    path('delete/<str:id>/',views.todo_delete,name='delete')
]
