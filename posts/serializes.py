from rest_framework import serializers

from .models import Post, Img, image, Comments
from accounts.models import Account



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class user(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'username', 'img']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class PostcommentSerializer(serializers.ModelSerializer):
    user = user(read_only=True)
    class Meta:
        model = Comments
        fields = ['id', 'comment', 'user','added_on']



# class Show(serializers.ModelSerializer):
#     user = user(read_only=True)
#     comment = PostcommentSerializer(read_only=True, many=True)
#     class Meta:
#         model = Post
#         fields = ['id' ,'article', 'created', 'user', 'comment',  'postlikes', 'postsaved', 'added_on']



class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = '__all__'


class ShowPostSerializer(serializers.ModelSerializer):
    user = user(read_only=True)
    comment = PostcommentSerializer(read_only=True, many=True)
    imgs = ImgSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ['id' ,'article', 'imgs', 'created', 'user', 'comment',  'postlikes', 'postsaved', 'added_on']


class imageserilaizer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = '__all__'

class SavedPostSerializer(serializers.ModelSerializer):
    saved = ShowPostSerializer(read_only=True)
    class Meta:
        model = Account
        fields = ['saved']