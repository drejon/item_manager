# Generated by Django 5.1.3 on 2025-03-31 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('item_id', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
