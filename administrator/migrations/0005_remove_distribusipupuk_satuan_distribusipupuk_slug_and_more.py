# Generated by Django 5.1.6 on 2025-02-22 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_remove_petani_kelompok_distribusipupuk_satuan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distribusipupuk',
            name='satuan',
        ),
        migrations.AddField(
            model_name='distribusipupuk',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='grup',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='lahan',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='distribusipupuk',
            name='jumlah',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='lahan',
            name='luas',
            field=models.CharField(max_length=20),
        ),
    ]
