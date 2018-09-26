from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import app.route

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            app.route.websocket_urlpatterns
        )
    ),
})