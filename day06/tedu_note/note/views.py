from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Note

# 校验登录装饰器
def check_login(fn):
    def wrap(request, *args, **kwargs):
        # 检查session
        if 'username' not in request.session or 'uid' not in request.session:
            #检查cookies
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                # 回写session
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)
    return wrap

# Create your views here.
@check_login
def list_view(request):
    uid = request.session['uid']
    all_note = Note.objects.filter(is_active=True, user_id=uid)
    return render(request, 'note/list_note.html', locals())

@check_login
def add_note(request):

    if request.method == 'GET':
        return render(request, 'note/add_note.html')

    elif request.method == 'POST':
        # 处理数据
        uid = request.session['uid']
        title = request.POST['title']
        content = request.POST['content']

        Note.objects.create(title=title, content=content, user_id=uid)
        #return HttpResponse('添加笔记成功')
        return HttpResponseRedirect('/note/all')

@check_login
def update_note(request, note_id):

    try:
        note = Note.objects.get(id=note_id, is_active=True)
    except Exception as e:
        print('---update note error is %s'%(e))
        return HttpResponse('note id is not existed')

    if request.method == 'GET':
        return render(request, 'note/update_note.html', locals())

    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        # 改
        note.title = title
        note.content = content
        note.save()

        return HttpResponseRedirect('/note/all')

@check_login
def page_note(request):
    # 获取url查询字符串book_id
    note_id = request.GET.get('note_id')
    if not note_id:
        return HttpResponse('---请求异常')
    try:
        note = Note.objects.get(id=note_id, is_active=True)
    except Exception as e:
        print('---delete book get error %s'%(e))
        return HttpResponse('---The book id is error')

    return render(request, 'note/page_note.html', locals())    

def del_note(request):
    # 获取url查询字符串book_id
    note_id = request.GET.get('note_id')
    if not note_id:
        return HttpResponse('---请求异常')
    try:
        note = Note.objects.get(id=note_id, is_active=True)
    except Exception as e:
        print('---delete book get error %s'%(e))
        return HttpResponse('---The book id is error')

    note.is_active = False
    note.save()

    return HttpResponseRedirect('/note/all')   