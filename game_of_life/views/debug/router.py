from ninja import Router
from game_of_life.views.debug.schema import PingResponse

debug_router = Router()


@debug_router.get("/ping")
def ping(
    request,
):
    return PingResponse(message="Hello World!")
