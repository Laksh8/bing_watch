# Generated by Django 2.2 on 2019-10-22 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0004_auto_20191014_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentlike',
            options={'ordering': ['-time']},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-time']},
        ),
        migrations.AlterModelOptions(
            name='videos',
            options={'ordering': ['-title']},
        ),
        migrations.AlterField(
            model_name='videos',
            name='likes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Likes', to=settings.AUTH_USER_MODEL),
        ),
    ]