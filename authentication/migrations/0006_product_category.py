# Generated by Django 4.0.5 on 2022-06-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_product_catogory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='None', max_length=200),
            preserve_default=False,
        ),
    ]