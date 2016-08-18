#coding:utf-8

import urllib
import urllib2
import json
no = '148540d0a5d811e4874000163e0026b6'
print '===============开始测试==========================='
test_data = {'no':'%s' % no,
             'user_id':'system@fuwo.com'
             }
headers = {'Content-Type': 'application/json'}
requrl = "http://3dtest.1jbest.com/yijiaifuwo/item/download/"
req = urllib2.Request(url = requrl,data =json.dumps(test_data), headers=headers)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res

print '===============下载接口测试完成====================='

test_data = {'no':'%s' % no,
             'user_id':'system@fuwo.com'
             }
# # headers = {'Content-Type': 'application/json'}
requrl = "http://3dtest.1jbest.com/yijiaifuwo/item/getcode/"
req = urllib2.Request(url=requrl, data=json.dumps(test_data), headers=headers)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res

print '===============获取录入码接口测试完成==================='

test_data = {'no': '%s' % no,
             'user_id' : 'system@fuwo.com'
             }
# headers = {'Content-Type': 'application/json'}
requrl = "http://3dtest.1jbest.com/yijiaifuwo/item/delete/"
req = urllib2.Request(url=requrl, data=json.dumps(test_data), headers=headers)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res

print '===============删除模型接口测试完成====================='

test_data = {'no': '%s' % no,
             'user_id': 'system@fuwo.com'
             }
# headers = {'Content-Type': 'application/json'}
requrl = "http://3dtest.1jbest.com/yijiaifuwo/item/revert/"
req = urllib2.Request(url=requrl, data=json.dumps(test_data), headers=headers)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res

print '===============恢复模型接口测试完成====================='

test_data = {'no': '%s' % no,
             'user_id': 'system@fuwo.com'
             }
# # headers = {'Content-Type': 'application/json'}
requrl = "http://3dtest.1jbest.com/yijiaifuwo/item/review/"
req = urllib2.Request(url=requrl, data=json.dumps(test_data), headers=headers)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res

print '===============重新审核模型接口测试完成=================='

test_data = {
             'user_id': 'system@fuwo.com','page':'1','count':'20'
             }
# # headers = {'Content-Type': 'application/json'}
requrl = "http://3dtest.1jbest.com/yijiaifuwo/item/list/"
req = urllib2.Request(url=requrl, data=json.dumps(test_data), headers=headers)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res

print '===============模型列表接口测试完成====================='

test_data = {
    'type': '2'
}
# headers = {'Content-Type': 'application/json'}
requrl = "http://3dtest.1jbest.com/yijiaifuwo/item/menu/"
req = urllib2.Request(url=requrl, data=json.dumps(test_data), headers=headers)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res

print '===============3D菜单列表接口测试完成===================='

print '================测试结束==============================='




