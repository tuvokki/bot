# Generated by Django 3.0.7 on 2020-06-05 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('answer', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntentPointer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pointer', models.CharField(max_length=200)),
                ('intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BotApp.Intent')),
            ],
        ),
    ]
