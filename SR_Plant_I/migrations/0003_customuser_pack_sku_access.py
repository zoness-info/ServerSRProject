# Generated by Django 5.0.6 on 2024-05-31 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SR_Plant_I', '0002_remove_customuser_app1_access_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Pack_sku_access',
            field=models.BooleanField(default=False, verbose_name="Pack_SKU's"),
        ),
    ]