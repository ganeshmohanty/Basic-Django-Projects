# Generated by Django 3.1.5 on 2021-05-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_product_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Fashion', 'Fashion')], default='Fashion', max_length=20),
        ),
    ]
