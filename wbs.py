#!/usr/bin/env python
# encoding=utf-8

from broswer import SunusBroswer
import simplejson as json
import pymongo

API_KEY            = 'YOUR_API_KEY'
SECRET             = 'YOUR_SECRET'
AUTH_HOST          = 'http://api.t.sina.com.cn/oauth/'
WEIBO              = 'http://www.weibo.com/'
CALLBACK_PAGE      = 'YOUR_CALLBACK'
user_comfire_page  = 'https://api.t.sina.com.cn/oauth2/authorize?client_id=%s&redirect_uri=%s&response_type=code&display=popup' % (API_KEY, CALLBACK_PAGE)
server_confirm_page= 'https://api.weibo.com/oauth2/access_token'
get_comment_url    = 'https://api.weibo.com/2/comments/show.json?access_token=%s&id=%s&page=%s'
AC_TOKEN = ''

def init():
    global AC_TOKEN
    print 'goto\n%s\nto get code.' % user_comfire_page
    code = raw_input('code:\n')
    print code
    data = {
            'client_id': API_KEY,
            'client_secret': SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': CALLBACK_PAGE
    }
    data = urllib.urlencode(data)
    broswer = SunusBroswer()
    resp = broswer.open(server_confirm_page, data=data).read_data()
    resp = json.loads(resp)
    AC_TOKEN = resp['access_token']
    if AC_TOKEN:
        print 'login successed'
        print AC_TOKEN

def get_comment(wbid, page):
    url = get_comment_url % (AC_TOKEN, wbid, page)
    print url
    broswer = SunusBroswer()
    resp = broswer.open(url).read_data()
    resp = json.loads(resp)
    cmts = []
    for c in resp['comments']:
        cmt = {
                'text': c['text'],
                'uname': c['user']['screen_name'],
                'uid': c['user']['idstr'],
                'cid': c['id'],
        }
        cmts.append(cmt)
    return cmts

def get_all_comments(wbid):
    start_page = 1
    db_host = 'localhost'
    db_port = 27017
    client = pymongo.MongoClient(db_host, db_port)
    wbdb = client.wbdb
    cmts_collection = wbdb.cmts
    while True:
        cmts = get_comment(wbid, start_page)
        print 'max_id', cmts[0]['cid']
        for c in cmts:
            cmts_collection.update(c, c, upsert=True)
        start_page += 1


if __name__ == '__main__':
    if not AC_TOKEN:
        init()
    get_all_comments('3658037472191026')
