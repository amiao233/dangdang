# Generated by Django 2.0.6 on 2019-05-27 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirm_string',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256, verbose_name='用户注册码')),
                ('code_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 't_confirm_string',
                'managed': False,
            },
        ),
    ]
