# Generated by Django 4.1.2 on 2022-10-25 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='library.category'),
        ),
    ]
