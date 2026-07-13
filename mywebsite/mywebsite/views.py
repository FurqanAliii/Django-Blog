from django.http import HttpResponse


def home(request):
    if request.method=='GET':
        print(request.headers)
        return HttpResponse(' Getting Hello Mr Baloch')
    else:
        return HttpResponse('Posting Mr Baloch')
    


def about(request):
    print(request.method)
    return HttpResponse('About Page')


def contact(request):
    print(request.path)
    print(request.GET)
    return HttpResponse('Contact Page')


def hello(request):
    print(request.user)
    return HttpResponse("Hello World!")