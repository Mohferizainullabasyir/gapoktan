# Generated by Django 5.1.6 on 2025-06-05 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0030_sppt_nama_ibu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sppt',
            name='petani',
        ),
    ]
