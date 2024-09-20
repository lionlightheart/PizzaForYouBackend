from django.db import models
import uuid

class Role(models.Model):
    role_id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    role_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role_name