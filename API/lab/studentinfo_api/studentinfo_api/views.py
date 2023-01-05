from django.http import JsonResponse
from .models import Student_info
from .serializers import Student_infoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def student_infolist(request):
    if request.method == 'GET':
        #grab all the data from database
        info = Student_info.objects.all()
        # call the class student_infoserializer in serializers.py
        serializer = Student_infoSerializer(info,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #get userdata and throgh serialize make it appropiate format and save in database
        serializer = Student_infoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data,status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors)  

@api_view(['GET','PUT','DELETE'])
def student_detail(request,id):
    try:
        info = Student_info.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':       
        serializer = Student_infoSerializer(info)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #get userdata and throgh serialize make it appropiate format and save in database
        serializer = Student_infoSerializer(info,data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    







    
    