from django.views.generic.base import View
from django.http.response import HttpResponse

# Create your views here.


class UserAuthAPIView(View):
    """用户权限"""

    def get(self, request):
        return HttpResponse('hello world')