# Generated by Django 2.2.5 on 2019-09-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_stud_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ganesh_puja', models.CharField(max_length=100)),
                ('Teachers_day', models.CharField(max_length=100)),
                ('Orientation', models.CharField(max_length=100)),
                ('Saraswati_puja', models.CharField(max_length=100)),
                ('Freshers', models.CharField(max_length=100)),
                ('Picnic', models.CharField(max_length=100)),
                ('Farewell', models.CharField(max_length=100)),
            ],
        ),
    ]
