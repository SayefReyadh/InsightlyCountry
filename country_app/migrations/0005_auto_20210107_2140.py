# Generated by Django 3.1.5 on 2021-01-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country_app', '0004_country_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=264),
        ),
    ]
