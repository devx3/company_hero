# Generated by Django 3.1.2 on 2020-10-02 13:58

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=18)),
                ('ie', models.CharField(max_length=20)),
                ('opened_date', models.DateField()),
                ('city', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employee', to='companies.company')),
            ],
            options={
                'verbose_name': 'Empregado',
                'verbose_name_plural': 'Empregados',
                'ordering': ['id'],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]