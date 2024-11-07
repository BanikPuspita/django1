# Generated by Django 5.1.2 on 2024-11-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('student_id', models.IntegerField()),
                ('dept', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
            ],
        ),
    ]
