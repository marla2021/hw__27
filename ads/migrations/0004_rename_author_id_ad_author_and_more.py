# Generated by Django 4.0.2 on 2022-02-24 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ad_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='ad',
            old_name='category_id',
            new_name='category',
        ),
    ]
