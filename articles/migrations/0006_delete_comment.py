# Generated by Django 4.2.10 on 2024-02-26 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_comment_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
