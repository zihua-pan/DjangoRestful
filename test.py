from django.conf import settings
from django.http import HttpResponse
from django.urls import path

setting = {
    'DEBUG': True,
    'ROOT_URLCONF': __name__
}

settings.configure(**setting)


def home(request):
    return HttpResponse('Hello world!')


urlpatterns = [
    path('', home,name='home'),
]

if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
