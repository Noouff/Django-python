# Generated by Django 3.1.7 on 2021-03-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_code',
            field=models.CharField(max_length=3, verbose_name='Emp code'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='fullname',
            field=models.CharField(max_length=100, verbose_name='الإسم الكامل'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(max_length=15, verbose_name='Mobile'),
        ),
    ]
