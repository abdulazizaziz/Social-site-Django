# Generated by Django 3.2.8 on 2021-10-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_comments_options'),
        ('accounts', '0013_alter_account_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='saved',
            field=models.ManyToManyField(blank=True, null=True, related_name='postsaved', to='posts.Post'),
        ),
    ]
