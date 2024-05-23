# Generated by Django 5.0.6 on 2024-05-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Packing', '0003_alter_printingrolldetail_grosswt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='printingrollbatch',
            name='createdat',
            field=models.DateTimeField(auto_now_add=True, default='2024-05-01', verbose_name='Created At'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='printingrollbatch',
            name='updatedat',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated AT'),
        ),
        migrations.AddField(
            model_name='printingrolldetail',
            name='createdat',
            field=models.DateTimeField(auto_now_add=True, default='2024-05-01', verbose_name='Created At'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='printingrolldetail',
            name='updatedat',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated AT'),
        ),
    ]
