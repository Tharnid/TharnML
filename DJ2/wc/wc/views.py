from django.http import HttpResponse

def homepage(request):
    # url request object
    return HttpResponse('Hello, from Django!!!')

def oatmeal(request):
    return HttpResponse('I love Oatmeal!!!')