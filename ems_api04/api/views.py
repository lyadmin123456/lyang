from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin
from rest_framework.views import APIView

from api.models import User, Employee
from api.serializers import UserModelSerializer, EmployeeModelSerializer
from utils.response import APIResponse


class UserAPIAView(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data
        serializer = UserModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        data = UserModelSerializer(user_obj).data
        return APIResponse(200, True, result=data)

    def get(self, request, *args, **kwargs):
        username = request.query_params.get('username')
        password = request.query_params.get('password')
        user_obj = User.objects.filter(username=username, password=password).first()
        if user_obj:
            data = UserModelSerializer(user_obj).data
            return APIResponse(200, True, result=data)
        return APIResponse(400, False)


# 员工页面查询添加

class EmployeeGenericAPIView(ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin,
                             GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    lookup_field = "id"

    # 查询所有员工
    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        return APIResponse(200, True, result=response.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        emp_obj = self.create(request, *args, **kwargs)
        return APIResponse(200, True, result=emp_obj.data)

    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return APIResponse(result=response.request.data)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return APIResponse(http_status=status.HTTP_400_BAD_REQUEST)