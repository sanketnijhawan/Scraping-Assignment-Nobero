# Generated by Django 5.1 on 2024-08-22 07:32

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
                ('title', models.CharField(max_length=255)),
                ('current_price', models.CharField(max_length=50)),
                ('mrp', models.CharField(max_length=50)),
                ('bought_count', models.CharField(max_length=50)),
                ('selected_color', models.CharField(max_length=50)),
                ('sizes', models.JSONField()),
                ('link', models.URLField(blank=True, max_length=500, null=True)),
                ('image_url', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]