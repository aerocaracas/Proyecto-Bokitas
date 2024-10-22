from django.urls import path
from tareas import views

urlpatterns = [

    path('tareas/', views.tareas, name='tareas'), 
    path('all_events/', views.all_events, name='all_events'), 
    path('add_event/', views.add_event, name='add_event'), 
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),

]