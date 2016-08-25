#coding:utf-8

import urllib
import urllib2
import json
print '===============开始测试==========================='
test_data = ['59596193526', '59597922100', '59620525284']
headers = {'Content-Type': 'application/json'}
requrl = "http://3dtest.1jbest.com/yijiaifuwo/item/modeltype/"
req = urllib2.Request(url = requrl,data =json.dumps(test_data), headers=headers)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res

print '=====================模型菜单测试完成=============='

test_data = ['YFNE-43-99-01', 'YFNE-43-88-01', 'YFNE-43-89-01']
headers = {'Content-Type': 'application/json'}
requrl = "http://3dtest.1jbest.com/yijiaifuwo/item/preview/"
req = urllib2.Request(url = requrl,data =json.dumps(test_data), headers=headers)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res

print '=====================获取预览图测试完成=============='

test_data = {'designerId':2,'salable':1,'product_name':'test','product_link':'http://www.test.com',
             'product_price':'90.2','unit':1,'discount_price':'20','is_public':1,'trim_width':11,'trim_length':11,'trim_height':11,
             'skucode':'123ss123'}
headers = {'Content-Type': 'application/json'}
requrl = "http://3dtest.1jbest.com/yijiaifuwo/item/update/"
req = urllib2.Request(url = requrl,data =json.dumps(test_data), headers=headers)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res

print '=====================新建物品测试完成==============='