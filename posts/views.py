from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import mixins

from .serializes import PostSerializer, ImgSerializer, ShowPostSerializer, imageserilaizer, CommentSerializer, PostcommentSerializer, SavedPostSerializer
from .models import Post, Img, image, Comments
from accounts.models import Account


# Create your views here.

@api_view(['GET'])
def post(request, id, formate=None):
    if request.method == 'GET':
        User = Account.objects.get(id=id)
        posts = Post.objects.all()
        obj = []
        for item in posts:
            if User.following.filter(id=item.user.id):
                serializer = ShowPostSerializer(item)
                obj.append(serializer.data)
        return Response(obj, status=status.HTTP_200_OK)
    

class createpost(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['POST'])
def updatepost(request, id, formate=None):
    post = Post.objects.get(id=id)
    post.article = request.data['article']
    post.save()
    serializer = ShowPostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)

class createpostimage(APIView):
    def get(self, request, formate=None):
        imgs = Img.objects.all()
        serializer = ImgSerializer(imgs, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        # data = JSONParser().parse(request)
        serializer = ImgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)



@api_view(['GET'])
def postimgs(resuest, formate=None):
    imgs = Img.objects.all()
    serializer = ImgSerializer(imgs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class image(viewsets.ModelViewSet):
    queryset = image.objects.all()
    serializer_class = imageserilaizer


@api_view(['GET'])
def getpost(request, id , formate=None):
    try:
        post = Post.objects.get(id=id)
    except:
        return Response('Post does not exits', status=status.HTTP_404_NOT_FOUND)
    serializer = ShowPostSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def somepost(request, username, formate=None):
    user = Account.objects.get(username=username)
    posts = Post.objects.filter(user=user.id)
    serializer = ShowPostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def deletepost(request, id, formate=None):
    post = Post.objects.get(id=id)
    post.delete()
    return Response('Deleteted', status=status.HTTP_200_OK)


@api_view(['POST'])
def addcomment(request, formate=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            comment = Comments.objects.get(id=serializer.data['id'])
            data = PostcommentSerializer(comment)
            return Response(data.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)

@api_view(['GET'])
def deletecomment(request, id, formate=None):
    comment = Comments.objects.get(id=id)
    comment.delete()
    return Response('Deleted Successfully')

@api_view(['POST'])
def editcomment(request, id, formate=None):
    comment = Comments.objects.get(id=id)
    comment.comment = request.data['comment']
    comment.save()
    serializer = PostcommentSerializer(comment)
    return Response(serializer.data)


@api_view(['GET'])
def addlike(request, id, postid, formate=None):
    user = Account.objects.get(id=id)
    user.likes.add(postid)
    return Response('Added', status=status.HTTP_200_OK)



@api_view(['GET'])
def removelike(request, id, postid, formate=None):
    user = Account.objects.get(id=id)
    user.likes.remove(postid)
    return Response('Removed', status=status.HTTP_200_OK)


@api_view(['GET'])
def addsaved(request, id, postid, formate=None):
    user = Account.objects.get(id=id)
    user.saved.add(postid)
    return Response('Added', status=status.HTTP_200_OK)



@api_view(['GET'])
def removesaved(request, id, postid, formate=None):
    user = Account.objects.get(id=id)
    user.saved.remove(postid)
    return Response('Removed', status=status.HTTP_200_OK)


@api_view(['GET'])
def savedpost(resuest, id, formate=None):
    user = Account.objects.get(id=id)
    posts = Post.objects.all()
    obj = []
    for item in posts:
        if user.saved.filter(id=item.id):
            serializer = ShowPostSerializer(item)
            obj.append(serializer.data)
    return Response(obj, status=status.HTTP_200_OK)