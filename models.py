from django.db import models
#from django.db import models
class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    studGrade=models.CharField(max_length=2)

    objects = models.Manager()
    def __str__(self):
        return self.firstName

class Teacher(models.Model):
    firstName = models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    TeacherSalary=models.CharField(max_length=10)

    objects = models.Manager()
    def __str__(self):
        return self.firstName

class Employee(models.Model):
    firstName = models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    EmployeeSalary=models.CharField(max_length=10)

    objects = models.Manager()
    def __str__(self):
        return self.firstName
     
# Create your models here.
