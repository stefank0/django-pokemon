# Generated by Django 3.0.6 on 2020-11-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0003_auto_20200704_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='drain',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='move',
            name='recoil',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='move',
            name='accuracy',
            field=models.IntegerField(),
        ),
    ]
