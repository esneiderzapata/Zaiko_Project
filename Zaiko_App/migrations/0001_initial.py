# Generated by Django 4.0.2 on 2022-03-23 14:13

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
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Zaiko_App/images/')),
                ('amount', models.IntegerField()),
                ('price', models.IntegerField()),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]