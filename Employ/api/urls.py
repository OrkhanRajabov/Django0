from django.urls import path
from Employ.api.views import DepartmentCreateReadApi,DepartmentUpdateDestroyApi,PositionCreateApiView,PositionRetrieveCreateApiView,EmployeeCreateApiView,EmployeeReitiveUpdateDeleteApiView

urlpatterns = [
    path("Department/",DepartmentCreateReadApi.as_view(),name = "Department"),
    path("Department/<int:pk>/",DepartmentUpdateDestroyApi.as_view(),name = "Update_Department"),
    path("Position/",PositionCreateApiView.as_view(),name = "Position"),
    path("Position/<int:pk>/",PositionRetrieveCreateApiView.as_view(),name =  "Position"),
    path("Employee/",EmployeeCreateApiView.as_view(),name = "Employee"),
    path("Employee/<int:pk>/",EmployeeReitiveUpdateDeleteApiView.as_view(),name = "Employee"),
]