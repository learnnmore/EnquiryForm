# Generated by Django 4.2.16 on 2024-10-12 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0002_remove_studentregistration_trainer_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentregistration',
            name='trainer_name',
        ),
        migrations.AddField(
            model_name='studentregistration',
            name='trainer_name',
            field=models.ManyToManyField(to='enquiries.trainer'),
        ),
    ]
