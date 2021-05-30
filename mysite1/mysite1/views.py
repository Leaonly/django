
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

POST_FROM = '''
<form method='post' action='/test_get_post'>
    用户名: <input type='text' name='uname'>
    <input type='submit' value=提交>
</form>
'''

def page_2003_view(request):
    html = "<h1>This is first page!</h1>"
    return HttpResponse(html)

def index_view(request):
    html = "<h1>This is index page!</h1>"
    return HttpResponse(html)

def page1_view(request):
    html = "<h1>This is first page!</h1>"
    return HttpResponse(html)

def page2_view(request):
    html = "<h1>This is second page!</h1>"
    return HttpResponse(html)

def pagen_view(request, pg):
    html = '<h1>This is %d page!</h1>' % (pg)
    return HttpResponse(html)

def aa_view(request, f1, aa, f2):
    if aa not in ['add', 'sub', 'mul']:
        return HttpResponse('argvs wrong!')

    if aa == 'add':
        bb = f1 + f2
    elif aa == 'sub':
        bb = f1 - f2
    elif aa == 'mul':
        bb = f1 * f2
    return HttpResponse(bb)

def cal2_view(request, x, op, y):
    html = 'x:%s op:%s y:%s'%(x, op, y)
    return HttpResponse(html)

def date_view(request, year, mon, day):
    html = '生日为： %s年%s月%s日'%(year, mon, day)
    return HttpResponse(html)

def test_request(request):
    print ('path info is ', request.path_info)
    print('method is ', request.method)
    print('questr is ', request.GET)
    print('full_path is ', request.get_full_path())
    print('ip is', request.META['REMOTE_ADDR'])

    #return HttpResponse('test request ok')
    return HttpResponseRedirect('/page/1')

def test_get_post(request):

    if request.method == 'GET':
        print(request.GET)
        print(request.GET['a'])
        print(request.GET.getlist('a'))
        print(request.GET.get('c', 'no c'))
        return HttpResponse(POST_FROM)

    elif request.method == 'POST':
        print('uname is ', request.POST['uname'])
        return HttpResponse('post is ok')
    else:
        pass

    return HttpResponse('--ok--')

def test_html(request):
    # 方案1
    # from django.template import loader
    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)

    # 方案2
    from django.shortcuts import render
    dic = {'username':'guoxiaonao','age':18}

    return render(request, 'test_html.html', dic )

def test_param(request):
    dic = {}
    dic['int'] = 88
    dic['str'] = 'hello'
    dic['script'] = '<script>alert(111)</script>'
    return render(request, 'test_html_param.html', dic)

def test_if_for(request):
        
        dic = {}
        dic['x'] = 10
        dic['lst'] = ['Tom', 'Jack', 'Lily']
        return render(request, 'test_if_for.html', dic)

def test_mycal(request):

    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == 'POST':
        # 处理计算
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']

        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x/y
        return render(request, 'mycal.html', locals())
            
def base_view(request):
    lst = ['Tom', 'Jack']
    return render(request, 'base.html', locals())

def music_view(request):

    return render(request, 'music.html')

def sport_view(request):

    return render(request, 'sport.html')

def test_url(request):

    return render(request, 'test_url.html')

def test_url_result(request, age):
    # 302跳转
    from django.urls import reverse
    url = reverse('base_index')
    return HttpResponseRedirect(url)

    #return HttpResponse('---test url res is ok')



