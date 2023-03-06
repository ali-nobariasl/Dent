from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>This is new dental project</h1>')