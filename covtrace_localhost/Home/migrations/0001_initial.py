# Generated by Django 4.1 on 2022-11-27 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New_Total_Number_Recovered_Patient',
            fields=[
                ('recorded_date', models.DateField(default=django.utils.timezone.now)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('barangay', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('date_admitted', models.DateField(blank=True, verbose_name='Date Admitted (mm/dd/yyyy):')),
                ('population', models.FloatField(default=1)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
            ],
        ),
    ]
