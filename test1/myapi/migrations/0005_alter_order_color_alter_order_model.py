# Generated by Django 4.1.2 on 2022-10-14 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_rename_vendor_id_model_vendor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.color'),
        ),
        migrations.AlterField(
            model_name='order',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.model'),
        ),
    ]
