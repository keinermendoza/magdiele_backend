from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.utils.text import Truncator

class Topic(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Tema"
        verbose_name_plural = "Temas"

class PostLatestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("-updated")
    # filter(is_public=True)

    

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                  related_name='post')
    
    title = models.CharField(verbose_name="Titulo", max_length=100)
    slug = models.SlugField(verbose_name="Fragmento", max_length=150, unique=True)
    subtitle = models.CharField(verbose_name="Subtitulo", max_length=300, null=True)
    body = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(verbose_name="Creado en", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Actualizado en", auto_now=True)
    image = models.ImageField(verbose_name="Imagen", upload_to='blog-images', null=True, blank=True)
    
    is_public = models.BooleanField(verbose_name="hacer visible para todos", default=False)
    topics = models.ManyToManyField(Topic,verbose_name="temas", related_name="posts")

    objects = models.Manager()
    latest = PostLatestManager()

    @property
    def short_body(self):
        return Truncator(self.body).words(20)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    class Meta:
        db_table = 'blog_post'
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
        verbose_name="Publicacion"
        verbose_name_plural = "Publicaciones"
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

class Comment(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                  related_name='comments')
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} commented {self.post.title}'

    class Meta:
        db_table = 'blog_comment'

        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
    
class Mensaje(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    # telefono = models.CharField(max_length=14)
    pregunta = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    visto = models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return f"{self.nombre} ha enviado un mensaje"

    class Meta:
        db_table = 'blog_mensaje'

        ordering = ['-fecha']
        indexes = [
            models.Index(fields=['-fecha'])
        ]
