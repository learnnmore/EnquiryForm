# Generated by Django 5.1.1 on 2024-09-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0003_studentregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('occupation', models.CharField(max_length=250)),
                ('experience', models.CharField(max_length=250)),
                ('batch_type', models.CharField(choices=[('weekday', 'Weekday'), ('weekend', 'Weekend')], default='weekday', max_length=10)),
                ('course', models.CharField(choices=[('select', 'Select'), ('python', 'Python'), ('java', 'Java'), ('data_science', 'Data Science'), ('dba', 'Database Administrator'), ('php', 'PHP')], default='select', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='course',
            field=models.CharField(choices=[('select', 'Select'), ('python', 'Python'), ('java', 'Java'), ('data_science', 'Data Science')], default='select', max_length=20),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='institute_reference',
            field=models.CharField(choices=[('select', 'Select'), ('online', 'Online Advertisement'), ('friend', 'Friend Referral'), ('social_media', 'Social Media'), ('other', 'Other')], default='select', max_length=20),
        ),
    ]
