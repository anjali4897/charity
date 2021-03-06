# Generated by Django 2.2.11 on 2020-03-15 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20200307_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='charity_list',
            fields=[
                ('ch_id', models.AutoField(primary_key=True, serialize=False)),
                ('ch_type', models.CharField(max_length=50)),
                ('ch_intro', models.TextField(max_length=500)),
                ('ch_about', models.TextField(max_length=500)),
                ('ch_address', models.TextField(max_length=500)),
                ('ch_contact', models.CharField(max_length=10)),
                ('ch_email', models.CharField(max_length=50)),
                ('ch_license', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('causes_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Causes')),
            ],
        ),
    ]
