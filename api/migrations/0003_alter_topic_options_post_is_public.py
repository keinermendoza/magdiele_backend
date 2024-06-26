# Generated by Django 5.0.6 on 2024-06-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_topic_post_topics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': 'Tema', 'verbose_name_plural': 'Temas'},
        ),
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='hacer visible para todos'),
        ),
    ]
