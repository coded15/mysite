# Generated by Django 3.2.11 on 2022-02-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediasettings',
            name='facebook',
            field=models.URLField(blank=True, help_text='Facebook URL', null=True),
        ),
        migrations.AddField(
            model_name='socialmediasettings',
            name='twitter',
            field=models.URLField(blank=True, help_text='Twitter URL', null=True),
        ),
    ]
