# Generated by Django 4.1.2 on 2022-10-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_hero_caurosel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='caurosel',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('', 'not active')], default='not active', max_length=254),
        ),
    ]
