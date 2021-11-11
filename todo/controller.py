from ninja import Router
from account.authorization import GlobalAuth
from .models import Todo
from django.contrib.auth import get_user_model
from .schemas import TodoOut, TodoCreate, TodoUpdate
from config.utils.schemas import MessageOut
from config.utils.middleware import check_pk
from typing import List
from django.shortcuts import get_object_or_404
from pydantic import UUID4


todo_controller = Router(tags=['todo'],auth=GlobalAuth())
User = get_user_model()

@todo_controller.get('',response={
    200:List[TodoOut],
    404:MessageOut,
    401:MessageOut
})
@check_pk
def list_todos(request):
    todos = Todo.objects.select_related('user').filter(user_id=request.auth['pk'])
    if todos:
        return todos
    return 404, {'message': 'Empty!'}

@todo_controller.post('', response={
    201:MessageOut,
    401:MessageOut,
    400:MessageOut
})
@check_pk
def create_todo(request, todo_in: TodoCreate):
    Todo.objects.create(**todo_in.dict(), user_id=request.auth['pk'])
    return 201, {'message':'Todo Created Successfully!'}

@todo_controller.get('{id}', response={
    200:TodoOut,
    404:MessageOut,
    401:MessageOut
})
@check_pk
def retrieve_todo(request,id: UUID4):
    return get_object_or_404(Todo, user_id=request.auth['pk'], id=id)

@todo_controller.put('{id}', response={
    200: MessageOut,
    400: MessageOut,
    401: MessageOut
})
@check_pk
def update_todo(request, id, finished: TodoUpdate):
    todo = get_object_or_404(Todo, user_id=request.auth['pk'], id=id)
    print(finished)
    todo.is_finished = finished.is_finished
    todo.save()
    return 200, {'message': 'Todo Updated Successfully!'}

@todo_controller.delete('{id}', response={
    200: MessageOut,
    400: MessageOut,
    401: MessageOut
})
@check_pk
def delete_todo(request, id):
    todo = get_object_or_404(Todo, user_id=request.auth['pk'], id=id)
    todo.delete()
    return 200, {'message': 'Todo Deleted Successfully!'}