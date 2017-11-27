import datetime
import hashlib
import hmac
import urllib
import base64
import random
import time

namespace = 'shivandersonservicebus'
queue_name = 'locustrequests'
key_name = 'policy'
shared_key = 'grtmBRbwTIQF/S1M7cHJlPz/WcQtFtJggW9l++7PmWQ='

def get_auth_token():
    """
    Returns an authorization token dictionary
    for making calls to Event Hubs REST API.
    """
    uri = build_host_name()
    uri = urllib.quote(uri, safe='')
    sas = shared_key.encode('utf-8')
    expiry = str(int(time.time() + 10000))
    string_to_sign = (uri + '\n' + expiry).encode('utf-8')
    signed_hmac_sha256 = hmac.HMAC(sas, string_to_sign, hashlib.sha256)
    signature = urllib.pathname2url(base64.b64encode(signed_hmac_sha256.digest()))
    return  {"namespace": namespace,
             "queue_name": queue_name,
             "token":'SharedAccessSignature sr={}&sig={}&se={}&skn={}' \
                     .format(uri, signature, expiry, key_name)
            }

def build_host_name():
    uri = 'https://' + namespace + '.servicebus.windows.net/' + queue_name
    return uri

# generating SAS token for later use
token_dict = get_auth_token()
token = token_dict['token']
