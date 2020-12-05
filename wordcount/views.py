from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fullText']
    # print(fulltext)
    wordlist = fulltext.split();

    return render(request,'count.html',{'fullText':fulltext,'count':len(wordlist)})

    # def homepage(request):
    # return render(request,'home.html',{"hithere":'this is jagrit'})