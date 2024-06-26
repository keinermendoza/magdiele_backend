# Generated by Django 5.0.6 on 2024-06-22 19:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=14)),
                ('consulta', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'blog_mensaje',
                'ordering': ['-fecha'],
                'indexes': [models.Index(fields=['-fecha'], name='blog_mensaj_fecha_c0caec_idx')],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Fragmento')),
                ('subtitle', models.CharField(max_length=300, null=True, verbose_name='Subtitulo')),
                ('body', models.TextField(verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado en')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado en')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog-images', verbose_name='Imagen')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
                'db_table': 'blog_post',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.post')),
            ],
            options={
                'db_table': 'blog_comment',
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-created'], name='blog_post_created_76eb4c_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['-created'], name='blog_commen_created_79f39f_idx'),
        ),
    ]
