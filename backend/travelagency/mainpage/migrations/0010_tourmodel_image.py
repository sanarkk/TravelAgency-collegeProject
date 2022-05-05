# Generated by Django 4.0.4 on 2022-05-05 11:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_remove_tourmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourmodel',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
