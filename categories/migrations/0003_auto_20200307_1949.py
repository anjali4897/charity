# Generated by Django 2.2.11 on 2020-03-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_causes'),
    ]

    operations = [
        migrations.AddField(
            model_name='causes',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='causes',
            name='desc',
            field=models.TextField(max_length=500),
        ),
    ]
