# Generated by Django 2.2 on 2022-11-21 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20221121_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.ImageField(upload_to='images/user/2022-11-21 13:21:58.446747/'),
        ),
    ]