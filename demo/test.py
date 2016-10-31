#encoding: utf-8
#!/usr/bin/python


import sys, urllib, urllib2, json
reload(sys)
sys.setdefaultencoding('utf8')

while True:
    url = 'http://apis.baidu.com/turing/turing/turing?key=879a6cb3afb84dbf4fc84a1df2ab7319&info=%s'

    info = raw_input().strip()

    url = url % info

    url.encode('utf-8')


    req = urllib2.Request(url)

    req.add_header("apikey", "619801c4f873d696f699a76dc0a5cec8")

    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        content = json.loads(content)
        print content['text']
        print type(content['text'])
        # content = dict(content)
        # print content['text']
