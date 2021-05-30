from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import User
import hashlib

# Create your views here.
def reg_view(request):

    # 注册
    # GET返回页面
    if request.method == 'GET':
        return render(request, 'user/register.html')
    
    # POST处理提交数据
    elif request.method == 'POST':
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
    # 1.两个密码要保持一致
    if password_1 != password_2:
        return HttpResponse('两次密码输入不一致')

    # 哈希算法 - 给定明文，计算出一段定长的不可逆值;md5,sha-256
    m = hashlib.md5()
    m.update(password_1.encode())
    password_m = m.hexdigest()

    # 2.当前用户名是否可用
    old_users = User.objects.filter(username=username)
    if old_users:
        return HttpResponse('用户名已注册')

    # 3.插入数据【暂时明文处理密码】
    try:
        user = User.objects.create(username=username, password=password_m)
    except Exception as e:
        # 有可能报错，重复插入【唯一索引注意并发写入问题】
        print('--create user error %s'%(e))
        return HttpResponse('用户名已注册')
        
    # 免登陆一天
    request.session['username'] = username
    request.session['uid'] = user.id
    #TODO 修改session存储时间为1天

    return HttpResponseRedirect('/index')

def login_view(request):

    if request.method == 'GET':
        # 检查登陆
        if request.session.get('username') and request.session.get('uid'):
            # return HttpResponse('已登录')
            return HttpResponseRedirect('/index')
        # 检查cookies
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            # 回写session
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            # return HttpResponse('已登录')
            return HttpResponseRedirect('/index')

        return render(request, 'user/login.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password_1']

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s'%(e))
            return HttpResponse('用户名或密码错误')

        # 比对密码
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('用户名或密码错误')

        # 记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id

        resp = HttpResponseRedirect('/index')

        # 判断用户是否点选checkbox
        if 'remember' in request.POST:
            resp.set_cookie('username', username)
            resp.set_cookie('uid', user.id, 3600*24*3)

        return resp

def logout_view(request):
    
    # 删除session
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    # 删除cookies
    resp = HttpResponseRedirect('/index')
    if 'username' in request.COOKIES:       
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')

    return resp

