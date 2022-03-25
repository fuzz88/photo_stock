from django.http import JsonResponse

from django.views import View


class Check(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": "online"})
 