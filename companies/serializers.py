from rest_framework import serializers
from .models import Company, Employee
from utils.cnpj import Cnpj


class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        many=True,
        read_only=False,
    )

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

    def validate_cnpj(self, value):
        if not Cnpj().validate(value):
            raise serializers.ValidationError('CNPJ Inválido.')
        return value
