# Generated by Django 2.1.7 on 2019-03-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20190313_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='code',
            field=models.CharField(default='Y74HjjTPXD84M08QyviI', max_length=20, unique=True, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='surveyanswer',
            name='code',
            field=models.CharField(default='eMz5JhMNgR31KY0XjtKd', max_length=20, verbose_name='code'),
        ),
    ]
