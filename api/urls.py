from django.urls import path
from rest_framework.authtoken import views as rest_views

from .views import (
    PostList,
    LatestPost,
    PostDetail,
    MensajeCreate,
    CommentList,
    CommentCreate,
    CommentRetriveUpdateDelete
) 
urlpatterns = [
    path('blog/', PostList.as_view(), name='post_list'),
    path('blog/latest/', LatestPost.as_view(), name='latest_post'),

    path('blog/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('blog/realizar/consulta/', MensajeCreate.as_view(), name='anonimo-msj'),
    path('blog/<slug:slug>/comments/', CommentList.as_view(), name='comment_list'),
    path('blog/<slug:slug>/comments/create/', CommentCreate.as_view(), name='comment_create'),
    path('blog/<slug:slug>/comments/<int:comment_id>', CommentRetriveUpdateDelete.as_view(), name='comment_detail'),

    path('login', rest_views.obtain_auth_token)



] 
