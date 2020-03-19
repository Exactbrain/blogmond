# Generated by Django 2.2.4 on 2020-03-19 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('body', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Quotes',
        ),
    ]
