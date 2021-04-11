from django.shortcuts import render, HttpResponse

# Create your views here.


def test_view(request):
    print('执行业务逻辑！')

    return HttpResponse("<h1>Hello World!</h1>")
