# Generated by Django 3.1.4 on 2020-12-12 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_auto_20201212_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_images'),
        ),
    ]
