from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer

from api.models import User, Employee


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'username': {
                'required': True,
                'min_length': 2,
                'error_messages': {
                    'required': '用户名必填',
                    'min_length': '用户长度不够'
                }
            },
            'real_name': {
                'required': True,
                'min_length': 2,
                'error_messages': {
                    'required': '真实姓名必填',
                    'min_length': '用户长度不够'
                }
            },
            'password': {
                'required': True,
                'max_length': 6,
                'min_length': 2,
                'error_messages': {
                    'required': '密码不能为空',
                    'min_length': '密码长度不够'
                }
            }
        }

    def validate_username(self, attrs):
        user = User.objects.filter(username=attrs).first()

        if user:
            raise exceptions.ValidationError("用户名已存在")

        return attrs

    def validate(self, attrs):
        password = attrs.get('password')
        req = self.context.get('request')
        re_pwd = req.data.get('pwd')
        if password != re_pwd:
            raise exceptions.ValidationError("两次密码不一致")
        return attrs

    def create(self, validated_data):
        return User.objects.create(validated_data)


# 员工信息查询
class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {
            'emp_name': {
                'required': True,
                'min_length': 2,
                'error_messages': {
                    'required': '用户名未填',
                    'min_length': '用户名过短'
                }
            },
            'salary': {
                'write_only': True,
                'error_messages':{
                    'required': '工资未填',
                }
            },
            'age': {
                'write_only': True,
                'required': '年龄为空',
            },
            'img': {
                'read_only': True
            }
        }
#
