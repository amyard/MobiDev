# Generated by Django 2.2.1 on 2019-05-22 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('implement', '0002_auto_20190521_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmodel',
            name='short_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]