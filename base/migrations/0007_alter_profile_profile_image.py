# Generated by Django 4.2.1 on 2023-06-12 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_profile_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='static/images/profile/default.png', upload_to='photos/profile/'),
        ),
    ]
