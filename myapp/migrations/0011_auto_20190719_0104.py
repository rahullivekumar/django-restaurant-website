# Generated by Django 2.2.2 on 2019-07-18 19:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_reserve_et'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='tt',
            field=models.CharField(choices=[(1, '9pm'), (2, '10pm')], default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reserve',
            name='dt',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='tableno',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='reserve',
            unique_together={('tableno', 'tt')},
        ),
        migrations.RemoveField(
            model_name='reserve',
            name='et',
        ),
    ]
