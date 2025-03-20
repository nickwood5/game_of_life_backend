from ninja import NinjaAPI
from game_of_life.views.debug.router import debug_router
from game_of_life.views.router import game_of_life_router

api = NinjaAPI()

api.add_router("/debug", debug_router)
api.add_router("/", game_of_life_router)
