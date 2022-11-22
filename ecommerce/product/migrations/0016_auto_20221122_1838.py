# Generated by Django 2.2 on 2022-11-22 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20221122_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='is_order',
        ),
        migrations.AddField(
            model_name='cart',
            name='is_not_order',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Cart'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/product/2022-11-22 18:38:07.023462/'),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='image',
            field=models.ImageField(upload_to='images/product/2022-11-22 18:38:07.023462/'),
        ),
    ]