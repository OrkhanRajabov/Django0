from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Datetime(models.Model):
    Created_at = models.DateField(auto_now_add = True)
    Updated_at = models.DateField(auto_now = True)

        
    

class Department(Datetime):
    Name = models.CharField(max_length= 200)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name_plural = "Departments"
        verbose_name = "Department"



class Position(Datetime):
    Name = models.CharField(max_length = 200)
    Salary = models.IntegerField()
    Department_id = models.ForeignKey(Department,on_delete = models.SET_NULL,null = True,blank = True )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name_plural = "Positions"
        verbose_name = "Position"
    


class Employee(Datetime):

    Status_choices = [
        ("Active","Active"),
        ("Retired","Retired"),
        ("Leave of Absence","Leave of Absence"),
    ]


    Name = models.CharField(max_length = 200)
    Surname = models.CharField(max_length = 200)
    Email = models.EmailField(unique = True)
    Department_id = models.ForeignKey(Department,on_delete = models.SET_NULL, null = True,blank = True)
    Position_id = models.ForeignKey(Position,on_delete = models.SET_NULL,null = True,blank = True)
    Status = models.CharField(choices = Status_choices,null = True,blank = True,max_length = 200)

    def __str__(self):
        return f"{self.Name},{self.Surname},{self.Email},{self.Status}"
    

    class Meta:
        verbose_name_plural = "Employes"
        verbose_name  =  "Employee"
