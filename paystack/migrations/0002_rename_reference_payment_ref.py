# Generated by Django 4.2.2 on 2023-06-18 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paystack', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='reference',
            new_name='ref',
        ),
    ]