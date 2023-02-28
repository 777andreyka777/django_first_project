from django.http import HttpResponse
from django.shortcuts import render 


def about(request):
    return HttpResponse('<h1>This is about page<h1/>')

def home(request):
    return render(request, 'home.html')

def reverse(request):
    text_input = request.GET['input']
    len_count = len(text_input.split())
    reverved_text = text_input[::-1]
    return render(request,'reverse.html',{'input': text_input, 'reversed_text': reverved_text, 'len_count': len_count})