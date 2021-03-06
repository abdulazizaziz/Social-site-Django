# Generated by Django 3.2.8 on 2021-10-23 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_comments_options'),
        ('accounts', '0012_account_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='postlikes', to='posts.Post'),
        ),
    ]
