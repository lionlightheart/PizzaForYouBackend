from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from .serializers import UserSerializer
import json

class UserView(View):

    def get(self, request) -> JsonResponse:
        # Para obtener el usuario por ID o todos los usuarios
        request_body = json.loads(request.body) if request.body else {} # Usar parámetros de consulta
        if "user_id" in request_body:
            try:
                user = User.objects.get(id=request_body["user_id"])
                serialized_user = UserSerializer(user)
                return JsonResponse(serialized_user.data, status=200)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
        else:
            users = User.objects.all()
            serialized_users = UserSerializer(users, many=True)
            return JsonResponse(serialized_users.data, safe=False, status=200)

    def post(self, request) -> JsonResponse:
        try:
            # Django ya maneja el cuerpo de la solicitud como JSON si usas Django REST Framework
            request_body = json.loads(request.body)  # Asegúrate de que request.body tenga contenido
            serialized_user = UserSerializer(data=request_body)
            if serialized_user.is_valid():
                serialized_user.save()
                return JsonResponse(serialized_user.data, status=201)
            else:
                return JsonResponse(serialized_user.errors, status=400)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': e.msg, 'docs': e.doc}, status=400)
