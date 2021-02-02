from dotenv import load_dotenv
load_dotenv()

from sanic import Sanic
from jinja2 import Environment, PackageLoader, select_autoescape
from blueprints.Home import HomeBP
from blueprints.API import APIBP


# -*- Sanic configg 4 fest deploiment -*-
app = Sanic(__name__)
app.static('/static', './static')
app.config.update({
    # "PROXIES_COUNT": 1,
    # "REAL_IP_HEADER": "X-Real-IP",
    # "FORWARDED_SECRET": "placeholder_secret"
})


# -*- Jinja2 setup -*-
J2env = Environment(loader=PackageLoader('server', './templates'),
                    autoescape=select_autoescape(['html', 'xml']),
                    enable_async=True)
J2env.globals["url_for"] = app.url_for
app.J2env = J2env


# -*- Blueprint Registration -*-
app.blueprint(HomeBP)
app.blueprint(APIBP)


# -*- DEBUG HEADERS -*-
@app.middleware('response')
async def debug_headers(request, response):
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    response.headers['Pragma'] = "no-cache"
    response.headers['Expires'] = "0"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, access_log=True, debug=True)
