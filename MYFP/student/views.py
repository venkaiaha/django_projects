from django.shortcuts import render

# Create your views here.
from .models import Student,Subject
from .serializers import StudentSerializer,SubjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
@api_view(['GET'])
def api_all_stud(request):
    objs=Student.objects.all()
    if objs:
        rest=StudentSerializer(objs,many=True)
        return Response(rest.data)
    else:
        return Response('No data found !')
@api_view(['GET'])
def api_all_subj(request):
    objs=Subject.objects.all()
    if objs:
        rest=SubjectSerializer(objs,many=True)
        return Response(rest.data)
    else:
        return Response('No data found !')

@api_view(['GET'])

def api_best_student_maths(request):
    all=Student.objects.all()
    if all:
        bsm=[]
        for i in all:
            if i.subject=='Mathematics':
                d={}
                d["sname"]=i.sname
                d["subject"]=i.subject
                d["marks"]=i.marks
                bsm.append(d)
                bsm.sort(key=lambda x:x['marks'],reverse=True)
    return JsonResponse(bsm[:5],safe=False)
bsm=Student.objects.filter(subject='Mathematics').aggregate(Max('marks'))