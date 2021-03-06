# Generated by Django 3.1.5 on 2021-01-07 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country_app', '0002_auto_20210107_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbour_name', models.CharField(max_length=264)),
            ],
        ),
        migrations.RemoveField(
            model_name='languagelist',
            name='topic',
        ),
        migrations.DeleteModel(
            name='NeighbourList',
        ),
        migrations.RemoveField(
            model_name='country',
            name='language',
        ),
        migrations.RemoveField(
            model_name='country',
            name='neighbour',
        ),
        migrations.AddField(
            model_name='country',
            name='language_list',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AddField(
            model_name='country',
            name='neighbour_list',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='timezones',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.DeleteModel(
            name='LanguageList',
        ),
        migrations.AddField(
            model_name='neighbour',
            name='country_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country_app.country'),
        ),
        migrations.AddField(
            model_name='language',
            name='country_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country_app.country'),
        ),
    ]
