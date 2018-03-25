from django.views.generic.base import View
from django.http.response import HttpResponse

# Create your views here.


class RoleAPIView(View):
    """用户角色"""

    def get(self, request):
        return HttpResponse('hello world')