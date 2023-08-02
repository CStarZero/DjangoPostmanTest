# Generated by Django 4.2.4 on 2023-08-01 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=600)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
