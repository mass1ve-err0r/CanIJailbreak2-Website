# -*- Blueprint setup -*-
from os import environ as env
from urllib.parse import unquote_plus
from sanic import Blueprint, response
from packaging.version import parse
from utils.jailbreaks import JailbreakMap as jMap
from utils.device_helper import DeviceMapPG as dMap
from utils.device_helper import DeviceMapPGNamed as aMap
from utils.device_helper import MinVersionMap as minMap
from utils.device_helper import MaxVersionMap as maxMap

APIBP = Blueprint('APIBP', version=1)
validTokens = [t for t in env.get("TOKENS").split("\n")]


# -*- Helper -*-
async def get_parsed_device(device):
    rv = [k for k, v in aMap.items() if device in v]
    if len(rv) == 0:
        return None
    return rv[-1]


# -*- Standard Routes -*-
@APIBP.route('/pls/<device_name>/<iosv>', methods=['GET'])
async def home2(request, device_name, iosv):
    device = unquote_plus(device_name)
    potentialToken = request.headers.get('Authorization')
    if potentialToken is None:
        return response.json({"status": -1})
    else:
        if potentialToken in validTokens:
            potentialDevice = await get_parsed_device(unquote_plus(device))
            if potentialDevice == None:
                return response.json({"status": 1})
            if parse(minMap.get(device)) <= parse(iosv) <= parse(maxMap.get(device)):
                supportedTools = [x for x in jMap if (parse(x.get('minimum_ios')) <= parse(iosv) <= parse(x.get('maximum_ios'))) \
                                  and (dMap.index(x.get('minimum_pg')) <= dMap.index(potentialDevice) <= dMap.index(x.get('maximum_pg')))]
                return response.json(
                    {
                        "status": 0,
                        "jelbreks": supportedTools
                    }
                )
            else:
                return response.json(
                    {
                        "status": 2,
                        "minimum_ios": minMap.get(device),
                        "maximum_ios": maxMap.get(device)
                    }
                )
        else:
            return response.json({"status": -1})
