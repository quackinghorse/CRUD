from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

def student_management(request):
    return render(request, 'index.html')

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request, pk =None):
    if request.method == 'GET':
        id = pk 
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=404)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        id = pk
        try:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)

    elif request.method == 'DELETE':
        id = pk
        try:
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response({'message': 'Student deleted successfully'})
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
