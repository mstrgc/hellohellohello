# Generated by Django 3.1.3 on 2020-11-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titanicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]