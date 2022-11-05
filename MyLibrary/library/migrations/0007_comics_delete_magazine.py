# Generated by Django 4.1.2 on 2022-10-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_magazine_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('author', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Magazine',
        ),
    ]
