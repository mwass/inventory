# Generated by Django 4.0.5 on 2022-07-07 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='data',
            new_name='date',
        ),
    ]