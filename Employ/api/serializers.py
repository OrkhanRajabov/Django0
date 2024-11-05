from rest_framework import serializers
from Employ.models import Department,Position,Employee


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ["id","Name","Created_at","Updated_at"]





class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ["id","Name","Salary","Department_id","Created_at","Updated_at"]


class EmployeeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Employee
        fields = ["id","Name","Surname","Email","Department_id","Position_id","Status","Created_at","Updated_at"]

