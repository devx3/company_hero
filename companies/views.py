from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Q


from .models import Company, Employee
from .serializers import (
    CompanySerializer,
    EmployeeSerializer,
)


class CompanyViewSet(viewsets.ModelViewSet):
    """All basic routes for company."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def retrieve(self, request, pk):
        """Retrieve either one user by ID or search for users by Username"""
        try:
            pk = int(pk)
            queryset = Employee.objects.filter(id=pk)
        except ValueError:
            pk = str(pk)
            queryset = Employee.objects.filter(
                Q(username__icontains=pk)
            )
        finally:
            if len(queryset) > 0:
                serializer = EmployeeSerializer(queryset, many=True, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({}, status=status.HTTP_404_NOT_FOUND)
