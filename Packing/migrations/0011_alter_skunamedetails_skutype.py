# Generated by Django 5.0.6 on 2024-06-06 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Packing', '0010_alter_skunamedetails_skutype_dispatchreq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skunamedetails',
            name='skutype',
            field=models.CharField(choices=[('POUCH', 'POUCH'), ('JAR', 'JAR'), ('PET', 'PET')], default='POUCH', max_length=50, verbose_name='SKU Type'),
        ),
    ]
