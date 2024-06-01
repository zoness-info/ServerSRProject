# Generated by Django 5.0.6 on 2024-06-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Packing', '0012_alter_skunamedetails_skutype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skunamedetails',
            name='skutype',
            field=models.CharField(choices=[('PET', 'PET'), ('JAR', 'JAR'), ('POUCH', 'POUCH')], default='POUCH', max_length=50, verbose_name='SKU Type'),
        ),
    ]
