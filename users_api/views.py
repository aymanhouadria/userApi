from drf_yasg.utils import swagger_auto_schema
from users_api import serializers
from rest_framework.response import Response
from rest_framework import status, generics
from users_api.models import User



class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @swagger_auto_schema(tags=['User'])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class GetUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @swagger_auto_schema(tags=['User'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class DeleteUsersView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @swagger_auto_schema(tags=['User'])
    def delete(self, request, *args, **kwargs):
        user_instance = self.get_object()
        self.perform_destroy(user_instance)
        self.perform_destroy(user_instance.address)

        return Response(status=status.HTTP_200_OK)



class UpdateUsersView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    http_method_names = ['put']

    @swagger_auto_schema(tags=['User'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class GetUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @swagger_auto_schema(tags=['User'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
