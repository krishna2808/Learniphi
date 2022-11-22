# Generated by Django 2.2 on 2022-11-22 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0008_auto_20221121_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/product/2022-11-22 16:20:35.189249/'),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='image',
            field=models.ImageField(upload_to='images/product/2022-11-22 16:20:35.189249/'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductProperty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]