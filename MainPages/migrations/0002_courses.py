# Generated by Django 3.2.3 on 2022-05-18 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=5)),
            ],
        ),
    ]