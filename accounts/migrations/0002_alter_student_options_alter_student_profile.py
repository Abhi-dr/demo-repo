# Generated by Django 4.2.22 on 2025-07-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterField(
            model_name='student',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='user_profile/'),
        ),
    ]
