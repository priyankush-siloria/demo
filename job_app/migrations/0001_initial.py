# Generated by Django 3.1 on 2020-08-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchedLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(blank=True, max_length=500, null=True)),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
