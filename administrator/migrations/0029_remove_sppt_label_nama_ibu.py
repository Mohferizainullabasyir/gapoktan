# Generated by Django 5.1.6 on 2025-06-05 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0028_sppt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sppt',
            name='label_nama_ibu',
        ),
    ]
