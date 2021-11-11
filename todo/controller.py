from ninja import Router
from account.authorization import GlobalAuth
from .models import Todo
from django.contrib.auth import get_user_model
from .schemas import TodoOut
from config.utils.schemas import MessageOut
from config.utils.middleware import check_pk


todo_controller = Router(tags=['todo'],auth=GlobalAuth())
User = get_user_model()

@todo_controller.get('',response={
    200:TodoOut,
    404:MessageOut,
    401:MessageOut
})
@check_pk
def list_todos(request):

    return Todo.objects.get(user__id=1)