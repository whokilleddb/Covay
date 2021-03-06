# Generated by Django 3.1.7 on 2021-04-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('just_co_away', '0005_auto_20210425_0914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='address_line_1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='cylinders_available',
            new_name='cylinders_per_customer',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='title',
        ),
        migrations.AddField(
            model_name='listing',
            name='verified_on',
            field=models.CharField(default='N/A', max_length=500),
        ),
        migrations.AlterField(
            model_name='listing',
            name='phone_number',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='listing',
            name='supplier',
            field=models.CharField(max_length=200),
        ),
    ]
