from django.shortcuts import render
import redis 
from .models import User
from django.http import HttpResponse

r = redis.Redis(host='192.168.170.136', port=6379, db=0, password='123456')


# Create your views here.
def user_detail(request, user_id):

    #/user/detail/1
    cache_key = 'user:%s'%(user_id)
    #优先查缓存
    if r.exists(cache_key):
        data = r.hgetall(cache_key)
        #{b'username':b'xxx', b'desc':b'xxx'}
        new_data = {k.decode():v.decode() for k, v in data.items()}
        username = new_data['username']
        desc = new_data['desc']
        html = 'cache username is %s ; desc is %s'%(username, desc)
        return HttpResponse(html)
        
    # 无缓存数据
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        print('---get user error is %s'%(e))
        return HttpResponse('---no user---')

    username = user.username
    desc = user.desc
    # 更新缓存
    r.hmset(cache_key,{'username':username,'desc':desc})
    r.expire(cache_key, 60)
    html = 'mysql username is %s ; desc is %s'%(username, desc)
    return HttpResponse(html)

def user_update(request):

    if request.method == 'GET':
        return render(request, 'user_update.html')
    elif request.method == 'POST':
        username = request.POST['username']
        desc = request.POST['desc']

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('---update get user error %s'%(e))
            return HttpResponse('---no user---')

        user.desc = desc
        user.save()

        # 删除缓存
        cache_key = 'user:%s' % (user.id)
        r.delete(cache_key)
        return HttpResponse('---update is ok ---')



