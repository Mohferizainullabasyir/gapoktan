# Generated by Django 5.1.6 on 2025-03-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0007_alter_ketuakelompok_email_alter_petani_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kesehatantanah',
            name='kadar_air',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='kesehatantanah',
            name='ph_tanah',
            field=models.CharField(max_length=100),
        ),
    ]
