import requests
import json
import sys
from datetime import datetime

class Connect:
    def __init__(self, url, username, passcode):
        PARAMS_TOKEN = {
            'action': "query",
            'meta': "tokens",
            'type': "login",
            'format': "json",
        }

        self.url = url
        self.session = requests.Session()

        try:
            ret = self.session.get(url, params=PARAMS_TOKEN)
            json_ret = ret.json()

            PARAMS_LOGIN = {
                'action': "login",
                'lgname': username,
                'lgpassword': passcode,
                'lgtoken': json_ret['query']['tokens']['logintoken'],
                'format':"json",
            }
            ret = self.session.post(url, data=PARAMS_LOGIN)
            json_ret = ret.json()
        except json.decoder.JSONDecodeError:
            print(f"Error decoding response from {url}.", file=sys.stderr)
        except Exception as err:
            print(f"Error opening session to {url}: {err}", file=sys.stderr)

    def get_wiki_page(self, page_title):
        params_parse_page = {
            'action':"parse",
            'page': page_title,
            'prop':"wikitext|revid|displaytitle",
            'format':"json",
        }
        try:
            ret = self.session.get(self.url, params=params_parse_page)
            ret_json = ret.json()

            wikipage = {
                'wikitext': str.encode(ret_json['parse']['wikitext']['*']),
                'revid': str(ret_json['parse']['revid']),
                'title': ret_json['parse']['displaytitle'],
                'pageid': str(ret_json['parse']['pageid'])
            }
            # Get the date of the last revision
            wikipage['date'] = self.get_page_revision_date(wikipage['pageid'],
                                                           wikipage['revid'])
            return wikipage
        except Exception as err:
            print(err, file=sys.stderr)
            return None

    def get_page_revision_date(self, pageid, revid):
        params_revision = {
            'action':"query",
            'prop':"revisions",
            'revids':f"{revid}",
            'rvprop':"timestamp",
            'format':"json",
        }
        try:
            ret = self.session.get(self.url, params=params_revision)
            ret_json = ret.json()
            ret_date = ret_json['query']['pages'][pageid]['revisions'][0]['timestamp']
            rev_date = datetime.strptime(ret_date, "%Y-%m-%dT%H:%M:%SZ")
            return rev_date
        except Exception as err:
            print(err, file=sys.stderr)
            return None
