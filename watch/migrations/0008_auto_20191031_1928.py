# Generated by Django 2.2 on 2019-10-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0007_reply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='videos',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]