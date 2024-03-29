# Generated by Django 3.2.12 on 2022-10-30 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('itemCategory', models.CharField(blank=True, choices=[('Refreshments', 'Refreshments'), ('Fast Food', 'Fast Food'), ('Lunch Plate', 'Lunch Plate'), ('Dinner Plate', 'Dinner Plate'), ('Indian Food', 'Indian Food'), ('Chinese Food', 'Chinese Food'), ('Soft Drinks', 'Soft Drinks')], max_length=100, null=True, verbose_name='Category')),
                ('itemPrice', models.IntegerField(blank=True, null=True, verbose_name='Price')),
                ('itemImage', models.ImageField(blank=True, null=True, upload_to='media/MenuImages', verbose_name='Image')),
                ('itemDescription', models.TextField(verbose_name='Description')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Menu Items',
            },
        ),
    ]
