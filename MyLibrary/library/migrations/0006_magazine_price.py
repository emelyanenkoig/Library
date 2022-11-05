# Generated by Django 4.1.2 on 2022-10-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_magazine'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='price',
            field=models.DecimalField(decimal_places=2, default=3000.0, max_digits=7),
            preserve_default=False,
        ),
    ]
