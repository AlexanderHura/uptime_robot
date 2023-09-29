
from django.http import HttpResponse
from core.services import Checker

def foo(request):
    checker= Checker()
    checker.generate_reports()
    return HttpResponse("Done")