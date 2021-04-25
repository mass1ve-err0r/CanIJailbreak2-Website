from dotenv import load_dotenv
from sanic import Sanic
from sanic.response import empty
from sanic.exceptions import SanicException
from jinja2 import Environment, PackageLoader, select_autoescape

# Environment prep before any stuff loads.
load_dotenv("./.env")

from blueprints.general import GeneralBP
from blueprints.api import APIBP


# -*- Server Config -*-
app = Sanic(__name__)
app.static('/static', './static')
app.config.update({
    # "PROXIES_COUNT": 1,
    # "FORWARDED_SECRET": "your_secret"
})


# -*- Jinja2 Setup -*-
J2Env = Environment(loader=PackageLoader('server', './templates'),
                    autoescape=select_autoescape(['html', 'xml']),
                    enable_async=True)
J2Env.globals["url_for"] = app.url_for
app.ctx.J2Env = J2Env


# -*- Blueprint Registration -*-
app.blueprint(GeneralBP)
app.blueprint(APIBP)


# -*- DEBUG HEADERS -*-
@app.middleware('response')
async def debug_headers(req, res):
    res.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    res.headers['Pragma'] = "no-cache"
    res.headers['Expires'] = "0"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=2, access_log=True, debug=True)
