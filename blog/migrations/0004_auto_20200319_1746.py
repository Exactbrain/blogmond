# Generated by Django 2.2.4 on 2020-03-19 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_breaking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tv',
            old_name='image',
            new_name='video',
        ),
    ]
