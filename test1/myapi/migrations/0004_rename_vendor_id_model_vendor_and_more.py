# Generated by Django 4.1.2 on 2022-10-11 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_rename_mod_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model',
            old_name='vendor_id',
            new_name='vendor',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='color_id',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='model_id',
            new_name='model',
        ),
    ]
