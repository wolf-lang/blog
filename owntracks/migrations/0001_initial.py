# Generated by Django 3.1.1 on 2021-02-26 02:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OwnTrackLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(max_length=100, verbose_name='用户')),
                ('lat', models.FloatField(verbose_name='纬度')),
                ('lon', models.FloatField(verbose_name='经度')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': 'OwnTrackLogs',
                'verbose_name_plural': 'OwnTrackLogs',
                'ordering': ['created_time'],
                'get_latest_by': 'created_time',
            },
        ),
    ]
