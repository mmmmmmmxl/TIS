from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
def testlogin(request,uid=''):
    user = User()
    user.id = uid
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request,user)
    return HttpResponseRedirect('/')