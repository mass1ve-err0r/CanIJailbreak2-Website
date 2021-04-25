# -*- Blueprint setup -*-
from sanic import Blueprint, response
from sanic.exceptions import NotFound
from packaging.version import parse
from utils.jailbreaks import JailbreakMap as jMap
from utils.device_helper import DeviceMapPG as dMap
from utils.device_helper import MinVersionMap as minMap
from utils.device_helper import MaxVersionMap as maxMap


GeneralBP = Blueprint('GeneralBP')
_tools14 = [x for x in jMap if parse(x.get('minimum_ios')) <= parse("14.0") <= parse(x.get('maximum_ios'))]
_tools13 = [x for x in jMap if parse(x.get('minimum_ios')) <= parse("13.0") <= parse(x.get('maximum_ios'))]
_tools12 = [x for x in jMap if parse(x.get('minimum_ios')) <= parse("12.0") <= parse(x.get('maximum_ios'))]
_tools11 = [x for x in jMap if parse(x.get('minimum_ios')) <= parse("11.0") <= parse(x.get('maximum_ios'))]
_tools10 = [x for x in jMap if parse(x.get('minimum_ios')) <= parse("10.0") <= parse(x.get('maximum_ios'))]
_tools9 = [x for x in jMap if parse(x.get('minimum_ios')) <= parse("9.0") <= parse(x.get('maximum_ios')) or parse("9.0") <= parse(x.get('maximum_ios')) <= parse("9.3.6")]
_tools8 = [x for x in jMap if parse(x.get('minimum_ios')) <= parse("8.0") <= parse(x.get('maximum_ios')) or parse("8.0") <= parse(x.get('maximum_ios')) <= parse("8.4")]
_tools7 = [x for x in jMap if parse(x.get('minimum_ios')) <= parse("7.0") <= parse(x.get('maximum_ios')) or parse("7.0") <= parse(x.get('maximum_ios')) <= parse("7.1.2")]
_tools6 = [x for x in jMap if parse(x.get('minimum_ios')) <= parse("6.0") <= parse(x.get('maximum_ios')) or parse("6.0") <= parse(x.get('maximum_ios')) <= parse("6.1.6")]


# -*- iPad Name Formatter -*-
async def format_ipad_name(name):
    if name == "iPad Pro 12.9 1":
        return "iPad Pro (12.9) (1.Generation)"
    elif name == "iPad Pro 12.9 2":
        return "iPad Pro (12.9) (2.Generation)"
    elif name == "iPad Pro 12.9 3":
        return "iPad Pro (12.9) (3.Generation)"
    elif name == "iPad Pro 12.9 4":
        return "iPad Pro (12.9) (4.Generation)"
    elif name == "iPad Pro 12.9 5":
        return "iPad Pro (12.9) (5.Generation)"
    elif name == "iPad Pro 11 1":
        return "iPad Pro (11) (1.Generation)"
    elif name == "iPad Pro 11 2":
        return "iPad Pro (11) (2.Generation)"
    elif name == "iPad Pro 11 3":
        return "iPad Pro (11) (3.Generation)"
    else:
        return name


# -*- Standard Routes -*-
@GeneralBP.route('/', methods=['GET'])
async def homepage(request):
    template = request.app.ctx.J2Env.get_template('/pages/Index.jinja2')
    page = await template.render_async(title="Home | Can I Jailbreak 2",
                                       tools14=_tools14,
                                       tools13=_tools13,
                                       tools12=_tools12,
                                       tools11=_tools11,
                                       tools10=_tools10,
                                       tools9=_tools9,
                                       tools8=_tools8,
                                       tools7=_tools7,
                                       tools6=_tools6)
    return response.html(page)


@GeneralBP.route('/guide-me', methods=['GET'])
async def guidance_get(request):
    template = request.app.ctx.J2Env.get_template('/pages/Guide.jinja2')
    page = await template.render_async(title="Jailbreak Wizard | Can I Jailbreak 2",
                                       dValue="5S-iPhone 5S",
                                       ios_version="7.0")
    return response.html(page)


@GeneralBP.route('/guide-me', methods=['POST'])
async def guidance_post(request):
    template = request.app.ctx.J2Env.get_template('/pages/Guide.jinja2')
    deviceName = request.form.get('devicePicker')
    deviceIOS = request.form.get('deviceIOS')
    if deviceName == None or deviceIOS == None:
        page = await template.render_async(title="Jailbreak Wizard | Can I Jailbreak 2",
                                           bannerType=3)
        return response.html(page)
    else:
        bannerType_ = 2
        deviceNameSplit = deviceName.split('-')
        devicePG = deviceNameSplit[0]
        deviceNameFormatted = await format_ipad_name(deviceNameSplit[1])
        if parse(minMap.get(deviceNameFormatted)) <= parse(deviceIOS) <= parse(maxMap.get(deviceNameFormatted)):
            supportedTools = [x for x in jMap if (parse(x.get('minimum_ios')) <= parse(deviceIOS) <= parse(x.get('maximum_ios'))) \
                              and (dMap.index(x.get('minimum_pg')) <= dMap.index(devicePG) <= dMap.index(x.get('maximum_pg')))]
            if len(supportedTools) != 0:
                bannerType_ = 1
            page = await template.render_async(title="Jailbreak Wizard | Can I Jailbreak 2",
                                               bannerType=bannerType_,
                                               jelbreks=supportedTools,
                                               device=deviceNameFormatted,
                                               ios_version=deviceIOS,
                                               dValue='-'.join(deviceNameSplit))
        else:
            page = await template.render_async(title="Jailbreak Wizard | Can I Jailbreak 2",
                                               bannerType=2,
                                               device=deviceNameFormatted,
                                               ios_version=deviceIOS,
                                               dValue='-'.join(deviceNameSplit))
    return response.html(page)


@GeneralBP.route('/tos', methods=['GET'])
async def privacy_policy(request):
    template = request.app.ctx.J2Env.get_template('/pages/Privacy.jinja2')
    page = await template.render_async(title="TOS & Privacy Policy | Can I Jailbreak 2")
    return response.html(page)


@GeneralBP.exception(NotFound)
async def site_exception(request, exception):
    _target = request.path.split('/')[1]
    if _target == 'v1':
        return response.json({"status": -1})
    template = request.app.ctx.J2Env.get_template('/pages/ErrorPage.jinja2')
    page = await template.render_async(title="Holy Papaya! | Can I Jailbreak 2")
    return response.html(page)
