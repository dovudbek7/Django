# Generated by Django 4.1.5 on 2023-03-13 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='review',
        ),
    ]
