# Generated by Django 5.0.3 on 2024-03-21 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
