import pathlib

from aiohttp import web
import aiohttp_cors

from smoothie.main.views import index

PROJECT_PATH = pathlib.Path(__file__).parent


def init_routes(app: web.Application) -> None:
    cors = aiohttp_cors.setup(app)
    # resource = cors.add(app.router.add_resource("/hello"))
    # route = cors.add(
    #     resource.add_route("GET", index), {
    #         "http://localhost:3000/": aiohttp_cors.ResourceOptions(
    #             expose_headers="*",
    #             allow_headers="*",
    #             allow_credentials=True,
    #             # max_age=3600,
    #         )
    #     })

    resource = cors.add(app.router.add_resource(''), {
        "*": aiohttp_cors.ResourceOptions(
            expose_headers="*",
            allow_headers="*",
            allow_credentials=True,
            allow_methods=["POST", "PUT", "GET"]),
    })
    resource.add_route("GET", index)


    # add_route = app.router.add_route
    #
    # add_route('*', '/', index, name='index')

    # added static dir
    app.router.add_static(
        '/static/',
        path=(PROJECT_PATH / 'static'),
        name='static',
    )
