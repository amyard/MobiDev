# Generated by Django 2.2.1 on 2019-05-21 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('implement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urlmodel',
            options={'ordering': ['-id'], 'verbose_name': 'URL', 'verbose_name_plural': 'URLS'},
        ),
        migrations.AlterField(
            model_name='urlmodel',
            name='short_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='urlmodel',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
