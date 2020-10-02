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

    def retrieve(self, request, pk):

        try:
            pk = int(pk)
            queryset = Employee.objects.filter(id=pk)
        except ValueError:
            pk = str(pk)
            queryset = Employee.objects.filter(
                Q(username__icontains=pk)
            )
        serializer = EmployeeSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
