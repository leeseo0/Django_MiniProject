from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<b>안녕?</b> 반가워.")

def test(request):
    return HttpResponse("나는 Test 페이지임")