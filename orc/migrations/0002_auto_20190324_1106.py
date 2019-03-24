# Generated by Django 2.0.13 on 2019-03-24 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='identificadorcartao',
            name='dono_cartao',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='identificadorcartao',
            name='nome_cartao',
            field=models.CharField(default='teste', max_length=50),
            preserve_default=False,
        ),
    ]
