# Generated by Django 3.1.2 on 2020-10-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20201002_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ManyToManyField(related_name='Employee', to='companies.Company'),
        ),
    ]