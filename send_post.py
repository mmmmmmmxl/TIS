import urllib
import urllib2
test_data = {'is_public':'1', 'userId':'749861', 'salable':'1', 'designer_id':'753324', 'is_active':'1',
             'sku_id':'123', 'product_name':'aaa', 'product_link':'http://wwww.ww.com', 'product_brand':'aaa',
             'cargo_no':'123', 'unit':'1', 'discount_price':'1', 'product_price':'12'
             }
test_data_urlencode = urllib.urlencode(test_data)
requrl = "http://192.168.3.132:8001/imerchant/admin/new/item/test/"
req = urllib2.Request(url = requrl,data =test_data_urlencode)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res