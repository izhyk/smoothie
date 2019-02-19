from typing import Dict

import aiohttp_jinja2
from aiohttp import web

from smoothie.constants import PROJECT_DIR


@aiohttp_jinja2.template('index.html')
async def index(request: web.Request) -> Dict[str, str]:
    return web.json_response({'text': 'hello world'})
