from django.http import HttpResponse


def home(req):
    return HttpResponse("Hello, world. This is the home page.")
