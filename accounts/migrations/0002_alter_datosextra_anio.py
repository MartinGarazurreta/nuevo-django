# Generated by Django 4.2.6 on 2023-11-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosextra',
            name='anio',
            field=models.DateField(null=True),
        ),
    ]
