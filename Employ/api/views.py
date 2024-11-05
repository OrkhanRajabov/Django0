from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from Employ.api.serializers import DepartmentSerializer,PositionSerializer,EmployeeSerializer
from Employ.models import Department,Position,Employee
from rest_framework.permissions import IsAdminUser,IsAuthenticated


class DepartmentCreateReadApi(ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset =  Department.objects.all()
    allowed_methods = ["GET","POST"]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = DepartmentSerializer
        return self.serializer_class
    

    

    

class  DepartmentUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    allowed_methods = ["PUT","PATCH","DELETE"]
    permission_classes = [IsAuthenticated]
    



class PositionCreateApiView(ListCreateAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    allowed_methods = ["GET","POST"]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = PositionSerializer
        return self.serializer_class
    

class PositionRetrieveCreateApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    allowed_methods = ["PUT","PATCH","DELETE"]
    permission_classes = [IsAuthenticated]


class EmployeeCreateApiView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    allowed_methods = ["GET","POST"]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = EmployeeSerializer
        return self.serializer_class
    

class EmployeeReitiveUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    allowed_methods = ["GET","PUT","PATCH","DELETE"]
    permission_classes = [IsAdminUser]



