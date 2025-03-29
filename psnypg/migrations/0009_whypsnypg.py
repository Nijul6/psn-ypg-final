# Generated by Django 5.1.6 on 2025-03-29 05:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psnypg', '0008_excosuser_excos_user_img'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyPSNYPG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('why_psnypg_title', models.CharField(max_length=255)),
                ('why_psnypg_description', models.TextField()),
                ('why_psnypg_slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('why_psnypg_img', models.ImageField(upload_to=' why_psnypg_images/')),
                ('why_psnypg_publish_date', models.DateTimeField(auto_now_add=True)),
                ('why_psnypg_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['why_psnypg_publish_date'],
            },
        ),
    ]
