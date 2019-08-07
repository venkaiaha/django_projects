from .models import SignUp
from .serializers import SignUpSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
def api_all(request):
    objs=SignUp.objects.all()
    if objs:
        rest=SignUpSerializer(objs,many=True)
        return Response(rest.data)
    else:
        return Response('No data Found !'), 200
@api_view(['POST'])
def api_add_new_user(request):
    name = request.POST.get("name", None)
    password = request.POST.get("password", None)
    new_user = SignUp.objects.create(name=name,
                                     password=password,
                                     )

    return Response({'message': 'new_user {:s} created'.format(new_user.name)}, status=200)

