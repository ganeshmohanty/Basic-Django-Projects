# Generated by Django 3.1.5 on 2021-05-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210503_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Gender',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women')], default='Men', max_length=10),
        ),
    ]