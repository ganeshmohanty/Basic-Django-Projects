# Generated by Django 3.1.5 on 2021-05-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_review_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]
