# Generated by Django 3.2.16 on 2022-10-28 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_auto_20221029_0023'),
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.restaurantowner'),
        ),
    ]