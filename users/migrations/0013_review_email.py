# Generated by Django 3.2.16 on 2023-01-13 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_review_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.EmailField(blank=True, max_length=500, null=True),
        ),
    ]
