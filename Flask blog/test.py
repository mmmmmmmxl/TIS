import urllib
import urllib2
test_data = {'mid':'myhome3d','uid':'753324','ammount':'1000'
             }
test_data_urlencode = urllib.urlencode(test_data)
requrl = "http://192.168.3.132:8001/imerchant/open/fcoin/save/"
req = urllib2.Request(url = requrl,data =test_data_urlencode)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res
