# Generated by Django 3.2.16 on 2022-12-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='name',
            field=models.CharField(default='Joe Bloggs', max_length=200),
        ),
    ]
