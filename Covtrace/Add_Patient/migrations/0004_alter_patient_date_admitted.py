# Generated by Django 4.1 on 2022-11-20 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Add_Patient', '0003_patient_date_admitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_admitted',
            field=models.DateField(blank=True, null=True, verbose_name='Date Admitted (mm/dd/yyyy)'),
        ),
    ]
