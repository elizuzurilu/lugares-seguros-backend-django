# Generated by Django 4.1.7 on 2023-03-09 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('description', models.CharField(max_length=256)),
                ('address_state', models.CharField(max_length=256)),
                ('address_city', models.CharField(max_length=256)),
                ('address_colonia', models.CharField(max_length=256)),
                ('address_street', models.CharField(max_length=256)),
                ('address_zipcode', models.CharField(max_length=256)),
            ],
        ),
    ]