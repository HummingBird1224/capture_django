# Generated by Django 2.2.7 on 2020-07-25 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCapture', '0006_auto_20200725_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Chapel', max_length=100),
            preserve_default=False,
        ),
    ]