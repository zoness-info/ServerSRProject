# Generated by Django 5.0.6 on 2024-06-02 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Packing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='srdailystockdetails',
            name='stockmode',
            field=models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening')], default='Morning', max_length=50, verbose_name='Morning/Evening'),
        ),
        migrations.AlterField(
            model_name='skunamedetails',
            name='skutype',
            field=models.CharField(choices=[('POUCH', 'POUCH'), ('JAR', 'JAR'), ('PET', 'PET')], default='POUCH', max_length=50, verbose_name='SKU Type'),
        ),
        migrations.AlterField(
            model_name='srdailystockdetails',
            name='stocktype',
            field=models.CharField(default='POUCH', max_length=50, verbose_name='Pouch/PET'),
        ),
    ]