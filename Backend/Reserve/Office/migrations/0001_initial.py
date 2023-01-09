# Generated by Django 4.1.5 on 2023-01-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FloorsDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField(choices=[(1, 'First floor'), (2, 'Second floor'), (3, 'Third floor')])),
                ('officeName', models.CharField(max_length=35)),
                ('equipment', models.BooleanField(default=True)),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
