# Generated by Django 4.0.2 on 2022-05-04 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zaiko_App', '0003_remove_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
