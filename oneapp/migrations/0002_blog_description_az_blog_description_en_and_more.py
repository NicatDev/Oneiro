# Generated by Django 5.0.6 on 2024-05-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_az',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
