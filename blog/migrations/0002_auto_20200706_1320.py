# Generated by Django 2.2.14 on 2020-07-06 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blogs',
            new_name='blog',
        ),
    ]
