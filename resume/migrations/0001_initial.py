# Generated by Django 4.1.2 on 2022-10-25 11:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=254)),
                ('daterange', models.CharField(blank=True, max_length=254)),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=254)),
                ('daterange', models.CharField(blank=True, max_length=254)),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, unique=True)),
                ('lvl', models.CharField(choices=[('50', '50'), ('60', '60'), ('70', '70'), ('80', '80'), ('90', '90'), ('100', '100')], default='50', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Sumary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=254)),
                ('text', models.TextField(blank=True)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('city', models.CharField(blank=True, max_length=254)),
                ('Degree', models.CharField(blank=True, max_length=254)),
                ('email', models.EmailField(default='0', max_length=254)),
                ('website', models.CharField(blank=True, max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('texttwo', models.CharField(blank=True, max_length=254)),
                ('textthree', models.CharField(blank=True, default='', max_length=254)),
            ],
        ),
    ]
