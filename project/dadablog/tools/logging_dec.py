from django.http.response import JsonResponse
from django.conf import settings
import jwt
from user.models import UserProfile

def logging_check(func):

    def wrap(request, *args, **kwargs):

        # 获取token request.META.get('HTTP_AUTHORIZATION')
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result = {'code':403, 'error':'pls login'}
            return JsonResponse(result)
        # 校验jwt
        try:
            res = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithms='HS256')
        except Exception as e:
            print('jwt decode error is %s'%(e))
            result = {'code':403, 'error':'pls login'}
            return JsonResponse(result)
        # 失败,返回code403 error:pls login

        # 获取登录用户
        username = res['username']
        user = UserProfile.objects.get(username=username)
        request.myuser = user
        return func(request, *args, **kwargs)

    return wrap