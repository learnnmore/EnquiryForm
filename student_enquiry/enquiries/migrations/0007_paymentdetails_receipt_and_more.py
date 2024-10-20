# Generated by Django 4.2.16 on 2024-10-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0006_remove_studentregistration_trainer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_mode', models.CharField(max_length=20)),
                ('payment_date', models.DateField()),
                ('receipt_no', models.IntegerField()),
            ],
            options={
                'db_table': 'payment_details',
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='batch_type',
            field=models.CharField(choices=[('all', 'All'), ('Weekday', 'Weekday'), ('Weekend', 'Weekend')], default='all', max_length=10),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='payment_mode',
            field=models.CharField(choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Cash', 'Cash'), ('Bank Transfer', 'Bank Transfer')], default='Cash', max_length=20),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='student_pincode',
            field=models.IntegerField(),
        ),
    ]
