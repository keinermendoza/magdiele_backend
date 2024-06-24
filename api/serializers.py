from django.core.mail import send_mail
from rest_framework import serializers
from .models import (
    Post,
    Comment,
    Mensaje,
    Topic
)
from account.serializers import UsernameSerializer

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["name"]

class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'pregunta']

    def save(self, **kwargs):
        instance =  super().save(**kwargs)
        self.send_abogada_message_email(instance)

    def send_abogada_message_email(self, message:Mensaje) -> None:
        """Sends an email when the feedback form has been submitted."""
        from dotenv import load_dotenv
        import os 
        load_dotenv()
        send_mail(
            f"Has recibido un mensaje de {message.nombre}",
            f"Responder al correo: {message.email}\nMensaje:\n{message.pregunta}",
            os.environ.get('EMAIL_HOST_USER'),
            [os.environ.get('EMAIL_OWNER')],
            fail_silently=False,
        )



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ListPostSerializer(serializers.ModelSerializer):
    topics = serializers.StringRelatedField(many=True)
    # updated = serializers.DateTimeField(format='%d-%m-%Y')
    class Meta:
        model = Post
        fields = ['id', 'slug', 'title', 'short_body', 'image', 'updated', 'topics']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class ComentSerializerGet(serializers.ModelSerializer):
    user = UsernameSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'body', 'user', 'created']

class ComentSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'body', 'user', 'created']

    def create(self, validated_data):
        # Obtiene el usuario autenticado desde el contexto
        user = self.context['user']
        post = self.context['post']  # Obtén el ID del post desde el contexto
        print(validated_data)
        

        # Crea y guarda el comentario con el usuario y el post
        comment = Comment(user=user, post=post, body=validated_data['body'])
        comment.save()
        return comment