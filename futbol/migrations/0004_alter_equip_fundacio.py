# Generated by Django 5.2.1 on 2025-05-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0003_alter_lliga_data_fi_alter_lliga_data_inici'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equip',
            name='fundacio',
            field=models.IntegerField(null=True),
        ),
    ]
