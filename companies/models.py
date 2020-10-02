from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Company(Base):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    ie = models.CharField(max_length=20)
    opened_date = models.DateField()
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['id']

    def __str__(self):
        return self.name


class Employee(User):
    company = models.ManyToManyField(Company, related_name="Employee")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Empregado'
        verbose_name_plural = 'Empregados'
        ordering = ['id']
