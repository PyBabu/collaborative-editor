from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/editor/<str:doc_id>/', consumers.DocumentConsumer.as_asgi()),
]