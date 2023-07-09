from django.http import HttpResponse
from django.shortcuts import render

def home(request):
#    data={
#        'home':'Welhome',
#       'studentlist':[
#            {'name':'Subhasish','ph':7029847241},
#            {'name':'Ram','ph':9635478229}
#        ]
#    }
    return render(request,"home.html")
def photo(request):
    return render(request,"photo.html")
def song(request):
    return render(request,"song.html")
def video(request):
    return render(request,"video.html")
def youtube(request):
    return render(request,"youtube.html")
def document(request):
    return render(request,"document.html")
def aboutus(request):
    return render(request,"about.html")