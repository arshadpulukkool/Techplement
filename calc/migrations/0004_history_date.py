# Generated by Django 5.0.2 on 2024-03-05 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
