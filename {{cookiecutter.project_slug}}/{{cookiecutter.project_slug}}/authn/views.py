from {{cookiecutter.project_slug}}.authn.models import User
from {{cookiecutter.project_slug}}.authn.serializers import UserSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework_roles.granting import is_self


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    view_permissions = {
        'destroy,retrieve': {'user': is_self, 'admin': True},
        'create': {'anon': True},
        'list': {'admin': True},
        'me': {'user': True},
    }

    @action(detail=False, methods=['GET'])
    def me(self, request):
        self.kwargs['pk'] = request.user.pk
        return self.retrieve(request)
