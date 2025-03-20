from django.urls import path
from game_of_life.views.websocket.ping_consumer import PingConsumer

websocket_urlpatterns = [
    path("api/ws/ping/", PingConsumer.as_asgi()),
]
