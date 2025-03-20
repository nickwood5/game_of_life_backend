from ninja import NinjaAPI
from game_of_life.views.debug.router import debug_router

api = NinjaAPI()

api.add_router("/debug", debug_router)
