import time
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

def test_cache(request):

    t = time.time()

    return HttpResponse('t is %s'%(t))