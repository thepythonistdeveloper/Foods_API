# Generated by Django 3.2.8 on 2022-01-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='photo',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
    ]
