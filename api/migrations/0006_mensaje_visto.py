# Generated by Django 5.0.6 on 2024-06-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_mensaje_pregunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='visto',
            field=models.BooleanField(default=False),
        ),
    ]
