# Generated by Django 3.2.5 on 2021-09-28 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210928_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='place',
        ),
    ]
