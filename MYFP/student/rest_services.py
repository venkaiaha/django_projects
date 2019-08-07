from .models import Student,Subject
from .serializers import StudentSerializer,SubjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from collections import defaultdict
@api_view(['GET'])
def api_all_student(request):
    obj=Student.objects.all()
    if obj:
        rest=StudentSerializer(obj,many=True)
        return Response(rest.data)
    else:
        return Response("No data Found !")
@api_view(['GET'])
def api_all_subject(request):
    obj=Subject.objects.all()
    if obj:
        rest=SubjectSerializer(obj,many=True)
        return Response(rest.data)
    else:
        return Response("No data Found !")

@api_view(['GET'])
def api_hsc(request):
    obj=Student.objects.all()
    hsc=defaultdict(int)
    for i in obj:
        hsc[i.sname] += int(i.marks)
    s=sorted(hsc.items(),key=lambda x:x[1],reverse=True)
    return Response(s[0])

@api_view(['GET'])
def api_lsc(request):
    obj=Student.objects.all()
    lsc=defaultdict(int)
    for i in obj:
        lsc[i.sname] += int(i.marks)
    s=sorted(lsc.items(),key=lambda x:x[1])
    return Response(s[0])
@api_view(['GET'])
def api_avg(request):
    obj=Student.objects.all()
    am=defaultdict(list)
    for i in obj:
        if i.marks>='40':
             am[i.subject].append(int(i.marks))
    av=defaultdict(int)
    for k,v in am.items():
        av[k]=sum(v)/len(v)
    return Response(av)
@api_view(['GET'])
def api_hpp(request):
    obj=Student.objects.all()
    obj1=Subject.objects.all()
    am=defaultdict(list)
    for i in obj:
        if i.marks>='40':
             am[i.subject].append(int(i.marks))
    av=defaultdict(int)
    for k,v in am.items():
        av[k]=sum(v)/len(v)
    s,a=max(av.items(),key=lambda x:x[1])
    for j in obj1:
        if j.subject==s:
            res=j.faculty
    return Response([res,s,a])
@api_view(['GET'])
def api_lpp(request):
    obj=Student.objects.all()
    obj1=Subject.objects.all()
    am=defaultdict(list)
    for i in obj:
        if i.marks<'40':
             am[i.subject].append(int(i.marks))
    # av=defaultdict(int)
    # for k,v in am.items():
    #     av[k]=sum(v)/len(v)
    s,a=max(am.items(),key=lambda x:sum(x[1]))
    for j in obj1:
        if j.subject==s:
            res=j.faculty
    return Response([res,s,a,len(a)])
@api_view(['GET'])
def api_hsc(request):
    obj=Student.objects.all()
    obj1=Subject.objects.all()
    hsc=defaultdict(list)
    for i in obj:
        if i.marks>'90':
            hsc[i.subject].append(int(i.marks))
    s,m=max(hsc.items(),key=lambda x:len(x[1]))
    for j in obj1:
        if j.subject==s:
            res=j.faculty
    return Response([res,s,m,len(m)])
@api_view(['GET'])
def api_bsm(request):
    obj=Student.objects.all()
    bsm=defaultdict(list)
    for i in obj:
        if i.subject=='Mathematics' and i.marks>'98':
            bsm[int(i.marks)].append(i.sname)
    return Response(bsm)
