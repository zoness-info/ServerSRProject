# Generated by Django 5.0.6 on 2024-05-23 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Packing', '0011_alter_printingrollbatch_operator_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrintingOperatorNameDetails',
            fields=[
                ('empid', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Employee ID')),
                ('operatorname', models.CharField(max_length=50, verbose_name='Operator Name')),
                ('mobileno', models.IntegerField(verbose_name='Mobile No')),
                ('createdat', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updatedat', models.DateTimeField(auto_now=True, verbose_name='Updated AT')),
                ('isdelete', models.BooleanField(default=False, verbose_name='Deleted')),
            ],
        ),
        migrations.RemoveField(
            model_name='printingrollbatch',
            name='operator_name',
        ),
        migrations.AddField(
            model_name='printingrollbatch',
            name='operatorname',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Packing.printingoperatornamedetails'),
            preserve_default=False,
        ),
    ]
