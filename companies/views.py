from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django.http import Http404


from .models import Company, Employee
from .serializers import (
    CompanySerializer,
    EmployeeSerializer,
)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def update(self, request, *args, **kwargs):
        print(request.data)
         # def save(self):
        #     employee = Employee(
        #         email=self.validated_data['email'],
        #         username=self.validated_data['username'],
        #         first_name=self.validated_data['first_name'],
        #         last_name=self.validated_data['last_name'],
        #         company=self.validated_data['company'],
        #     )

        #     password = self.validated_data['password']
        #     password2 = self.validated_data['password2']

        #     if password != password2:
        #         raise serializers.ValidationError({'password': 'As senhas precisam ser iguais'})

        #     employee.set_password(password)
        #     employee.save()
        #     return employee
        # serializer = self.serializer_class(EmployeeSerializer, data=request.data, partial=True)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(request.data, status=status.HTTP_200_OK)
