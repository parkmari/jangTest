# Generated by Django 3.1.7 on 2021-03-17 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=999),
            preserve_default=False,
        ),
    ]
