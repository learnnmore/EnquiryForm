# Generated by Django 4.2.16 on 2024-10-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0007_paymentdetails_receipt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='receipt_year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
