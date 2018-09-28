# Generated by Django 2.1.1 on 2018-09-28 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20180919_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(default='938449ad-8560-4626-8e5e-078389f2664f', on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
