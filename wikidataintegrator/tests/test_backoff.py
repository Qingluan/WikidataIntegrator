import json

import requests
import sys

from wikidataintegrator import wdi_login
from wikidataintegrator.backoff.wdi_backoff import wdi_backoff
from wikidataintegrator.wdi_config import config
from wikidataintegrator.wdi_core import WDItemEngine


@wdi_backoff()
def test_bad_json():
    json.loads("<xml>I failed :(</xml>")


@wdi_backoff()
def test_bad_request():
    requests.get("http://www.fakeurlgsdkjhjgfseg.com")


def test_bad_login():
    config['BACKOFF_MAX_TRIES'] = 4
    config['BACKOFF_MAX_VALUE'] = 2
    wdi_login.WDLogin("name", "pass", server="www.wikidataaaaaaaaa.org")

def test_item():
    config['BACKOFF_MAX_TRIES'] = 4
    config['BACKOFF_MAX_VALUE'] = 2
    wd_item = WDItemEngine(wd_item_id="Q14911732", server='www.wikidataaaaaaaaa.org', search_only=True)
    print(wd_item.get_label('en'))

if __name__ == "__main__":
    if sys.argv[1] == "json":
        test_bad_json()
    if sys.argv[1] == "request":
        test_bad_request()
    if sys.argv[1] == "login":
        test_bad_login()
    if sys.argv[1] == "item":
        test_item()