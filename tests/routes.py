from yrouter import route

from .handlers import hello_user, home

routes = (
    route("/", home),
    route("hello/<str:username>/", hello_user),
)
