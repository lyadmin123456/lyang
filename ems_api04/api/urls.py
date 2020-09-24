from django.urls import path
from api import views

urlpatterns = [
    path('users/', views.UserAPIAView.as_view()),
    path('users/<str>:id/', views.UserAPIAView.as_view()),

    #     员工路径
    path('emps/', views.EmployeeGenericAPIView.as_view()),
    path('emps/<str:id>/', views.EmployeeGenericAPIView.as_view())
]
