# Generated by Django 5.0.1 on 2024-02-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
