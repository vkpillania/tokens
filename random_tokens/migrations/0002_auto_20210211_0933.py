# Generated by Django 2.2.7 on 2021-02-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('random_tokens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokens',
            name='live_till',
            field=models.IntegerField(null=True),
        ),
    ]
