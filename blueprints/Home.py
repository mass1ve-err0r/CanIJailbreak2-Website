# -*- Blueprint setup -*-
from packaging.version import parse
from sanic import Blueprint
from sanic.response import html, json
from sanic.exceptions import NotFound

from utils.SiteHelper import JailbreakMap as jMap
from utils.SiteHelper import DeviceMap as dMap


HomeBP = Blueprint("HomeBP")
_tools14 = [x for x in jMap if parse(x.get('minIOS')) <= parse("14.0") <= parse(x.get('maxIOS'))]
_tools13 = [x for x in jMap if parse(x.get('minIOS')) <= parse("13.0") <= parse(x.get('maxIOS'))]
_tools12 = [x for x in jMap if parse(x.get('minIOS')) <= parse("12.0") <= parse(x.get('maxIOS'))]
_tools11 = [x for x in jMap if parse(x.get('minIOS')) <= parse("11.0") <= parse(x.get('maxIOS'))]
_tools10 = [x for x in jMap if parse(x.get('minIOS')) <= parse("10.0") <= parse(x.get('maxIOS'))]
_tools9 = [x for x in jMap if parse(x.get('minIOS')) <= parse("9.0") <= parse(x.get('maxIOS')) or parse("9.0") <= parse(x.get('maxIOS')) <= parse("9.3.6")]
_tools8 = [x for x in jMap if parse(x.get('minIOS')) <= parse("8.0") <= parse(x.get('maxIOS')) or parse("8.0") <= parse(x.get('maxIOS')) <= parse("8.4")]
_tools7 = [x for x in jMap if parse(x.get('minIOS')) <= parse("7.0") <= parse(x.get('maxIOS')) or parse("7.0") <= parse(x.get('maxIOS')) <= parse("7.1.2")]
_tools6 = [x for x in jMap if parse(x.get('minIOS')) <= parse("6.0") <= parse(x.get('maxIOS')) or parse("6.0") <= parse(x.get('maxIOS')) <= parse("6.1.6")]


# -*- Routes -*-
@HomeBP.route('/')
async def index(request):
    template = request.app.J2env.get_template('/pages/Index.jinja2')
    _html = await template.render_async(title="Home | Can I Jailbreak2",
                                        tools14=_tools14,
                                        tools13=_tools13,
                                        tools12=_tools12,
                                        tools11=_tools11,
                                        tools10=_tools10,
                                        tools9=_tools9,
                                        tools8=_tools8,
                                        tools7=_tools7,
                                        tools6=_tools6)
    return html(_html)


@HomeBP.route('/guide-me-please', methods=['GET', 'POST'])
async def guide_me(request):
    template = request.app.J2env.get_template('/pages/Guide.jinja2')
    _html = None
    if request.method == 'POST':
        ident_device_full = request.form.get('devicePicker')
        ident_ios = request.form.get('deviceIOS')
        if ident_ios == None or ident_device_full == None:
            _html = await template.render_async(title="Jailbreak Wizard | Can I Jailbreak2",
                                                showFieldError=True)
        else:
            ident_device_split = ident_device_full.split('-')
            ident_device = ident_device_split[0]
            ident_device_name = ident_device_split[1]
            _found = False
            map_supported = [x for x in jMap if (parse(x.get('minIOS')) <= parse(ident_ios) <= parse(x.get('maxIOS'))) \
                             and (dMap.index(str(x.get('minProc'))) <= dMap.index(str(ident_device)) <= dMap.index(str(x.get('maxProc'))))]
            if len(map_supported) != 0:
                _found = True
            _html = await template.render_async(title="Jailbreak Wizard | Can I Jailbreak2",
                                                showResult=_found,
                                                iosV=ident_ios,
                                                dev=ident_device_name,
                                                jelbreks=map_supported)
    elif request.method == 'GET':
        _html = await template.render_async(title="Jailbreak Wizard | Can I Jailbreak2")
    return html(_html)


@HomeBP.route('/privacy-policy')
async def privacy(request):
    template = request.app.J2env.get_template('/pages/Privacy.jinja2')
    _html = await template.render_async(title="Privacy | Can I Jailbreak2")
    return html(_html)


@HomeBP.exception(NotFound)
async def site_exception(request, exception):
    _target = request.path.split('/')[1]
    if _target == 'v1':
        return json({"status": "-1"})
    template = request.app.J2env.get_template('/pages/NF.jinja2')
    _html = await template.render_async(title="Holy Papaya! | Can I Jailbreak2")
    return html(_html)
