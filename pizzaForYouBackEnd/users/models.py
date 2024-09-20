import uuid
from django.db import models
from roles.models import Role

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rol= models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True, related_name='roles') 

    def __str__(self):
        return self.username
    
