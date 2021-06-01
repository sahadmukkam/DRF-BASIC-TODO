
from .models import Task
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serializers import TaskSerializers
@api_view(['GET'])
def todo_view(request):
    todo=Task.objects.all()
    serializer=TaskSerializers(todo,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def todo_create(request):
    serializer=TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def todo_one(request,id):
    todo=Task.objects.get(id=id)
    serializers=TaskSerializers(todo,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def todo_update(request,id):
    todo=Task.objects.get(id=id)
    serializer=TaskSerializers(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def todo_delete(request,id):
    todo=Task.objects.get(id=id)
    todo.delete()
    todo1=Task.objects.all()
    serializer=TaskSerializers(todo1,many=True)
    return Response(serializer.data)






