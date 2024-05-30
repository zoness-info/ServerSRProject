# Generated by Django 5.0.6 on 2024-05-29 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Packing', '0003_alter_ppsrdetails_ipk1_runningsku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk10_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ipk_10_machinename', to='Packing.packingmachinedetails'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk10_operatorname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ipk_10_operatorname', to='Packing.operatornamedetails'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk10_plan',
            field=models.IntegerField(blank=True, null=True, verbose_name='IPK10 Plan'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk10_pouchcount',
            field=models.IntegerField(blank=True, null=True, verbose_name='IPK10 Pouch Count'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk10_runningsku',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ipk_10_runningsku', to='Packing.skunamedetails'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk10_status',
            field=models.CharField(blank=True, choices=[('OFF', 'OFF'), ('ON', 'ON')], default='OFF', max_length=50, null=True, verbose_name='IPK10 ON or OFF Status'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk11_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ipk_11_machinename', to='Packing.packingmachinedetails'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk11_operatorname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ipk_11_operatorname', to='Packing.operatornamedetails'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk11_plan',
            field=models.IntegerField(blank=True, null=True, verbose_name='IPK11 Plan'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk11_pouchcount',
            field=models.IntegerField(blank=True, null=True, verbose_name='IPK11 Pouch Count'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk11_runningsku',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ipk_11_runningsku', to='Packing.skunamedetails'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk11_status',
            field=models.CharField(blank=True, choices=[('OFF', 'OFF'), ('ON', 'ON')], default='OFF', max_length=50, null=True, verbose_name='IPK11 ON or OFF Status'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk2_status',
            field=models.CharField(blank=True, choices=[('OFF', 'OFF'), ('ON', 'ON')], default='OFF', max_length=50, null=True, verbose_name='IPK2 ON or OFF Status'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk3_status',
            field=models.CharField(blank=True, choices=[('OFF', 'OFF'), ('ON', 'ON')], default='OFF', max_length=50, null=True, verbose_name='IPK3 ON or OFF Status'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk4_status',
            field=models.CharField(blank=True, choices=[('OFF', 'OFF'), ('ON', 'ON')], default='OFF', max_length=50, null=True, verbose_name='IPK4 ON or OFF Status'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk5_status',
            field=models.CharField(blank=True, choices=[('OFF', 'OFF'), ('ON', 'ON')], default='OFF', max_length=50, null=True, verbose_name='IPK5 ON or OFF Status'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk6_status',
            field=models.CharField(blank=True, choices=[('OFF', 'OFF'), ('ON', 'ON')], default='OFF', max_length=50, null=True, verbose_name='IPK6 ON or OFF Status'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk7_status',
            field=models.CharField(blank=True, choices=[('OFF', 'OFF'), ('ON', 'ON')], default='OFF', max_length=50, null=True, verbose_name='IPK7 ON or OFF Status'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk8_status',
            field=models.CharField(blank=True, choices=[('OFF', 'OFF'), ('ON', 'ON')], default='OFF', max_length=50, null=True, verbose_name='IPK8 ON or OFF Status'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk9_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='IPK_9_machinename', to='Packing.packingmachinedetails'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk9_operatorname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ipk_9_operatorname', to='Packing.operatornamedetails'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk9_plan',
            field=models.IntegerField(blank=True, null=True, verbose_name='IPK9 Plan'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk9_pouchcount',
            field=models.IntegerField(blank=True, null=True, verbose_name='IPK9 Pouch Count'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk9_runningsku',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ipk_9_runningsku', to='Packing.skunamedetails'),
        ),
        migrations.AlterField(
            model_name='ppsrdetails',
            name='ipk9_status',
            field=models.CharField(blank=True, choices=[('OFF', 'OFF'), ('ON', 'ON')], default='OFF', max_length=50, null=True, verbose_name='IPK9 ON or OFF Status'),
        ),
    ]