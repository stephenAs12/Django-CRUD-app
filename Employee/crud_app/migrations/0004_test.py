# Generated by Django 5.0.2 on 2024-03-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0003_alter_employee_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=20)),
                ('lName', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'test_table',
            },
        ),
    ]