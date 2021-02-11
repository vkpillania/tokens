# Generated by Django 2.2.7 on 2021-02-11 09:28

from django.db import migrations, models
import time


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('token', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('is_block', models.BooleanField(default=False)),
                ('generated', models.IntegerField(default=time.time)),
                ('live_till', models.IntegerField()),
            ],
            options={
                'db_table': 'tokens',
                'managed': True,
            },
        ),
    ]
