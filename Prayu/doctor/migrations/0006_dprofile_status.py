# Generated by Django 2.2.4 on 2019-11-12 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_auto_20191112_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='dprofile',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
