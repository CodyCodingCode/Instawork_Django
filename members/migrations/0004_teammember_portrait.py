# Generated by Django 4.2.7 on 2023-12-01 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_teammember_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='portrait',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
