# Generated by Django 2.2.2 on 2019-07-18 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20190719_0106'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reserve',
            unique_together={('tableno', 'tt', 'dt')},
        ),
    ]