from rest_framework import serializers
from .models import Company, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='companies-detail')

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'company',
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': False,
            }
        }


class CompanySerializer(serializers.ModelSerializer):
    employees = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='employees-detail')

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'cnpj',
            'ie',
            'opened_date',
            'city',
            'region',
            'email',
            'phone',
            'employees',
        )
