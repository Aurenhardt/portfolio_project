# Generated by Django 3.0.6 on 2020-06-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overviewpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='PostCategory',
            field=models.CharField(choices=[('0', 'General'), ('1', 'Armor Concepts'), ('2', 'Portraits'), ('3', 'Character Design'), ('4', 'Posters')], default='0', max_length=20),
        ),
    ]
