# Generated by Django 5.0.7 on 2024-08-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment_is_approved_post_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
    ]
