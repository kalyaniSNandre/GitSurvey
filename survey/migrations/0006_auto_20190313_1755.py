# Generated by Django 2.1.7 on 2019-03-13 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20190313_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='code',
            field=models.CharField(default='gKFZAZeejpLRHInFBtPg', max_length=20, unique=True, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='surveyanswer',
            name='code',
            field=models.CharField(default='24HltlFc0pkXN0XLSZv5', max_length=20, verbose_name='code'),
        ),
    ]
