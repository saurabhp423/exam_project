# Generated by Django 3.1.1 on 2020-10-11 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_auto_20201011_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='email',
            new_name='username',
        ),
    ]