# Generated by Django 2.2.2 on 2019-07-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20190718_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='dt',
            field=models.DateTimeField(),
        ),
    ]
