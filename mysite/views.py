# render shortcut actually renders the HTML / CSS files properly
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# test for static content
# 'request' means the actual user's data request to the server
def index(request):
    return render(request, 'mysite/index.html')

def login(request):
    return render(request, 'mysite/login.html')

#def manage(request):
#    return render(request, 'mysite/manage.html')

# index function that displays stuff on browsers
# takes parameter 'request' that is sent
# and then returns the Hello World message
#def home(request):
#    return HttpResponse('Hello World')