# Generated by Django 3.2.9 on 2022-11-05 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20221031_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='college',
            field=models.TextField(max_length=124, null=True),
        ),
    ]
