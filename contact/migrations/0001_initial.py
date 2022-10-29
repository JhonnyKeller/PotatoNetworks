# Generated by Django 4.1.2 on 2022-10-27 14:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDataTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('service_pack', models.CharField(choices=[('Basic', 'Basic'), ('Standard', 'Standard'), ('Gold', 'Gold'), ('Custom', 'Custom')], default='Basic', max_length=254)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('text', models.TextField(default='')),
                ('status', models.CharField(choices=[('awaiting response', 'awaiting response'), ('responded', 'responded'), ('banned message', 'banned message')], default='awaiting response', max_length=254)),
                ('schedule', models.CharField(choices=[('Lisbon Time 08:00h', 'Lisbon Time 08:00h'), ('Lisbon Time 09:00h', 'Lisbon Time 09:00h'), ('Lisbon Time 10:00h', 'Lisbon Time 10:00h'), ('Lisbon Time 11:00h', 'Lisbon Time 11:00h'), ('Lisbon Time 12:00h', 'Lisbon Time 12:00h'), ('Lisbon Time 14:00h', 'Lisbon Time 14:00h'), ('Lisbon Time 15:00h', 'Lisbon Time 15:00h'), ('Lisbon Time 16:00h', 'Lisbon Time 16:00h'), ('Lisbon Time 18:00h', 'Lisbon Time 18:00h')], default='Lisbon Time 08:00h', max_length=254)),
                ('file', models.FileField(blank=True, upload_to='contact_files')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_option', to='services.servicespages')),
            ],
        ),
    ]
