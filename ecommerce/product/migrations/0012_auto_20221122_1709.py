# Generated by Django 2.2 on 2022-11-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20221122_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/product/2022-11-22 17:09:14.709599/'),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='image',
            field=models.ImageField(upload_to='images/product/2022-11-22 17:09:14.709599/'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]