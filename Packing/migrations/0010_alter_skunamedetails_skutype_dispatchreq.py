# Generated by Django 5.0.6 on 2024-06-04 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Packing', '0009_alter_skunamedetails_skutype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skunamedetails',
            name='skutype',
            field=models.CharField(choices=[('JAR', 'JAR'), ('PET', 'PET'), ('POUCH', 'POUCH')], default='POUCH', max_length=50, verbose_name='SKU Type'),
        ),
        migrations.CreateModel(
            name='DispatchReq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Requirement Date')),
                ('reqbox', models.IntegerField(verbose_name='Requirement Box')),
                ('skuname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Packing.skunamedetails')),
            ],
        ),
    ]