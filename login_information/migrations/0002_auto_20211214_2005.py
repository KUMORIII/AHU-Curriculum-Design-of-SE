# Generated by Django 3.2.8 on 2021-12-14 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_information', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentinfo',
            options={'managed': True, 'verbose_name_plural': '学生信息表'},
        ),
        migrations.RemoveField(
            model_name='checkinfo',
            name='check_time',
        ),
    ]
