# Generated by Django 2.2.5 on 2019-09-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=100)),
                ('roll', models.IntegerField(unique=True)),
                ('sem', models.IntegerField()),
            ],
        ),
    ]
