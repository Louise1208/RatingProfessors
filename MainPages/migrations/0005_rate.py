# Generated by Django 3.2.3 on 2022-05-18 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainPages', '0004_auto_20220518_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0, max_length=1)),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainPages.courses')),
            ],
        ),
    ]
