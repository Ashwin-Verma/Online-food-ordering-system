# Generated by Django 3.0.4 on 2020-07-26 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200726_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='status',
        ),
    ]
