from mycoolproject.auth.models import User
from mycoolproject.auth.serializers import UserSerializer

from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()