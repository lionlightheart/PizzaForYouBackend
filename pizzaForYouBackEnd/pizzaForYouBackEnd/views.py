from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views import View

class OtherViews(View):

    def get(self, request) -> JsonResponse:
        token=get_token(request)
        return JsonResponse({'csrf_token': token}, status=200)