# Generated by Django 3.1.7 on 2021-02-26 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premontagem', '0002_auto_20210225_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='qrcode',
        ),
        migrations.AddField(
            model_name='bike',
            name='barcode',
            field=models.ImageField(blank=True, upload_to='barcodes/'),
        ),
    ]