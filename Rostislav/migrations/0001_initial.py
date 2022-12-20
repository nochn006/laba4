# Generated by Django 3.2.16 on 2022-12-12 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('name', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('release', models.IntegerField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.company')),
            ],
        ),
    ]
