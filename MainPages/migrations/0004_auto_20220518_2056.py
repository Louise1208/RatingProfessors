# Generated by Django 3.2.3 on 2022-05-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPages', '0003_courses_taught_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='semester',
            field=models.IntegerField(default=1, max_length=1),
        ),
        migrations.AddField(
            model_name='courses',
            name='year',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='courses',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
