# Generated by Django 5.0.1 on 2024-02-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0003_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='option1',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option2',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option3',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option4',
            field=models.CharField(max_length=70),
        ),
    ]
