import urllib
from urllib import parse
from urllib import request
import json

# 定数宣言
ENCODING = 'utf-8'
METHOD = 'POST'


def func_post_slack(token_url, text):
    """slackm¥に投稿を行う
    入力:
    url: トークンのurl
    text: 辞書型{text: 'string'}

    """ 
    json_byte = json.dumps(text).encode(ENCODING)
    req = request.Request(token_url, data=json_byte, method=METHOD)
    urllib.request.urlopen(req)


