from django.contrib import admin
from Employ.models import Department,Position,Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id","Name","Created_at","Updated_at"]
    list_display_links = ["id","Name"]



@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["id","Name","Salary","Department_id","Created_at","Updated_at"]
    list_display_links = ["id","Name","Department_id"]



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id","Name","Surname","Email","Department_id","Position_id","Status","Created_at","Updated_at"]
    list_display_links  = ["id","Name","Email","Department_id","Position_id"]