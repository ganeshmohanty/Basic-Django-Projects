# Generated by Django 3.1.5 on 2021-05-02 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210501_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='star',
            field=models.IntegerField(default=1),
        ),
    ]
