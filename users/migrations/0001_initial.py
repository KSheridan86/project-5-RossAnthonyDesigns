# Generated by Django 3.2.16 on 2022-12-27 14:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newsletter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
