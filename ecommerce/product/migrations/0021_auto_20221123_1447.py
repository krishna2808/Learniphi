# Generated by Django 2.2 on 2022-11-23 09:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20221123_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/product/2022-11-23 14:47:22.009792/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/product/2022-11-23 14:47:22.010402/'),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='image',
            field=models.ImageField(upload_to='images/product/2022-11-23 14:47:22.010402/'),
        ),
    ]
