from pysimplesoap.client import SoapClient

import json
import urllib
import sys
import os

def octopart2data(part_num, octo_token=None):
    data = None

    if octo_token == None:
        # search the api token in envs
        octo_token = os.environ.get('OCTO_TOKEN')

    queries = [
        {'sku': part_num},
        ]

    url = 'http://octopart.com/api/v3/parts/match?queries=%s' \
        % urllib.quote(json.dumps(queries))
    url += '&apikey={}&include[]=descriptions'.format(octo_token)

    data = urllib.urlopen(url).read()
    response = json.loads(data)
    print response
    mpn = response['results'][0]['items'][0]['mpn']   # horrible and fixed
    #description = response['results'][0]['descriptions'][0]

    print json.dumps(response, indent=2)

    return None
    print mpn, description

    data = {
        "provider": "octopart",
        "provider_pn": None,
        "manufacturer_pn": mpn,
        "description": description
    }

    return None
