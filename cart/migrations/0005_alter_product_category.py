# Generated by Django 5.0.3 on 2024-03-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Bed', 'Bed'), ('Sofa', 'Sofa'), ('Table', 'Table'), ('Living Room', 'Livin Room'), ('Bed Room', 'Bed Room')], max_length=20),
        ),
    ]
