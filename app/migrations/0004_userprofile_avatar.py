# Generated by Django 2.2.7 on 2021-01-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_add_country_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
