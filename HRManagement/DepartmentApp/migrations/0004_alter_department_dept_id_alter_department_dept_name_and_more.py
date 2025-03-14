# Generated by Django 5.1.3 on 2024-11-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DepartmentApp', '0003_alter_department_dept_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='dept_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
