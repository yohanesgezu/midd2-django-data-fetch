from django.urls import pathfrom . impor
t views
from .views import EmployeeDelete
from .views import TeacherDelete
from .views import StudeDelete
import os.path
urlpatterns = [
     path('', views.apiOverview, name="api-overview"),
     path('student-list/', views.studentList, name="student-list"),
     path('TeacherList/', views.TeacherList, name="Teacher-list"),
     path('EmployeeList/', views.EmployeeList, name="employee-list"),
     path('EmployeeListDelete/<str:pk>/', views.EmployeeDelete.as_view(), name="delete"),
     path('TeacherDelete/<str:pk>/', views.TeacherDelete.as_view(), name="delete"),
     path('StudentDelete/<str:pk>/', views.StudeDelete.as_view(), name="delete"),

     
    
#      path('student-list/<str:pk>/', views.detailView, name='student-detail'),
#      path('student-delete/<str:pk>/', views.delateView , name='student-delete'),
#      path('student-create/', views.createView, name='student-create'),
#      path('student-update/<str:pk>/', views.updateView, name='student-update')
 ]
