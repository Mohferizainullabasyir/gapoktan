# Generated by Django 5.1.6 on 2025-05-19 08:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0021_remove_ketuakelompok_email_remove_petani_email_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumDiskusi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('isi', models.TextField()),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_diskusi', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Forum Diskusi',
            },
        ),
        migrations.CreateModel(
            name='KomentarDiskusi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isi', models.TextField()),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='komentar', to='administrator.forumdiskusi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='komentar_diskusi', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Komentar Diskusi',
            },
        ),
    ]
