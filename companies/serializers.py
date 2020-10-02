from rest_framework import serializers
from .models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
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
        )


class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), many=True)

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
            'password': {'write_only': True}
        }

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
