# Generated by Django 5.0.1 on 2024-02-21 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0018_book2'),
    ]

    operations = [
        migrations.CreateModel(
            name='employeeBooks',
            fields=[
            ],
            options={
                'ordering': ['salary'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('dbapp.employee',),
        ),
    ]
