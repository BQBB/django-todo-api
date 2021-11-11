from django.db import models
from django.contrib.auth import get_user_model
from config.utils.models import Entity

User = get_user_model()

class Todo(Entity):
    title = models.CharField(max_length=255)
    description = models.TextField('description')
    is_finished = models.BooleanField('is_finished',default=False)
    user = models.ForeignKey(User,verbose_name='user',related_name='todos',on_delete=models.CASCADE)