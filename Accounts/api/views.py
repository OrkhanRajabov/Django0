from Accounts.models import User
from Accounts.api.serializers import UserSerializers
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


class UserListCreateApiView(ListCreateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    allowed_methods = ["GET","POST"]
    permission_classes = [IsAuthenticated]
    

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = UserSerializers
        return self.serializer_class
    

    
    