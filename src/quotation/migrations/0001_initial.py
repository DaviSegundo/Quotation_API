# Generated by Django 3.2 on 2022-01-12 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('date', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('response_date', models.JSONField()),
            ],
        ),
    ]