from django.shortcuts import render
from django.http import HttpResponse


from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import mixins



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


from .models import Account, Notification
from posts.models import Post
from .serializers import (
    AccountSerializer, ShowAccountSerializer,
    Following, AccountEditSerializer,
    AccountTopSerializer, NotificationtSerializer,
    NotificationtCreateSerializer
)
from posts.serializes import user



# Create your views here.

class UserApi(APIView):
    def post(self, request, formate=None):
        data = request.data
        account = Account.objects.simplecreate(
            password=data['password'],
            email=data['email'],
            username=data['username'],
            name=data['name'],
            gender=data['gender']
            )
        account.save()
        return Response('Created', status=status.HTTP_200_OK)

class UsernameCheck(APIView):
    def post(self, request, formate=None):
        data = JSONParser().parse(request)
        username = data['username']
        account = Account.objects.filter(username=username)
        print(bool(account))
        if account:
            return Response(False)
        return Response(True)




class MYTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['name'] = user.name
        return token

class Token(TokenObtainPairView):
    serializer_class = MYTokenSerializer

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = self.get_serializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            return Response('Wrong')

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def showuser(request, username):
    user = Account.objects.get(username=username)
    serializer = ShowAccountSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def showuserid(request, id):
    user = Account.objects.get(id=id)
    serializer = ShowAccountSerializer(user)
    return Response(serializer.data)



@api_view(['GET'])
def getfollowing(request, id, formate=None):
    user = Account.objects.get(id=id)
    following = user.following.all()
    obj = []
    for item in following:
        if item.id != id:
            new = Following(item)
            obj.append(new.data)
    return Response(obj)



@api_view(['GET'])
def getfollower(request, id, formate=None):
    user = Account.objects.get(id=id)
    following = user.follow.all()
    obj = []
    for item in following:
        if item.id != id:
            new = Following(item)
            obj.append(new.data)
    return Response(obj)



@api_view(['GET'])
def getuser(request, id, formate=None):
    try:
        account = Account.objects.get(id=id)
    except:
        return Response('User does not exits', status=status.HTTP_404_NOT_FOUND)
    serializer = user(account)
    return Response(serializer.data)


@api_view(['GET'])
def addfollow(request, id, add, formate=None):
    user = Account.objects.get(id=id)
    user.following.add(add)
    return Response('Successfully')

@api_view(['GET'])
def removefollow(request, id, remove, formate=None):
    user = Account.objects.get(id=id)
    user.following.remove(remove)
    return Response('Successfully')



def show(request):
    user = Account.objects.all()
    return render(request, 'index.html', {'text': user})


class Editaccount(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Account.objects.all()
    serializer_class = AccountEditSerializer


@api_view(['GET'])
def usernameuniqe(request, username, formate=None):
    isuser = Account.objects.filter(username=username)
    return Response(bool(isuser))


@api_view(['GET'])
def emailuniqe(request, email, formate=None):
    isuser = Account.objects.filter(email=email)
    return Response(bool(isuser))

@api_view(['GET'])
def topuser(request, formate=None):
    queryset = Account.objects.all()
    serializer = AccountTopSerializer(queryset, many=True)
    return Response(serializer.data[:7])


class NotiPost(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class  = NotificationtCreateSerializer

@api_view(['GET'])
def notification(request, id, formate=None):
    notifications = Notification.objects.filter(to_user=id)
    serializer = NotificationtSerializer(notifications, many=True)
    return Response(serializer.data)
