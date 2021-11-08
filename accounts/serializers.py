from rest_framework import serializers

from .models import Account, Notification

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class ShowAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id' ,'name', 'username', 'following','gender', 'img', 'country', 'live_city', 'live_country', 'birth', 'education', 'number', 'single', 'about', 'age']
        



class Following(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name', 'username', 'img']


class AccountEditSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Account
        fields = ['id' ,'name', 'username', 'img', 'country', 'live_city', 'live_country', 'birth', 'education', 'number', 'single', 'about']


class AccountTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id' ,'name', 'username', 'following', 'follow', 'gender', 'img', 'country', 'live_city', 'live_country', 'birth', 'education', 'number', 'single', 'about', 'age']


class NotificationtSerializer(serializers.ModelSerializer):
    from_user = ShowAccountSerializer()
    class Meta:
        model = Notification
        fields = ['id', 'from_user', 'to_user', 'read', 'iSfollow', 'likedpost']


class NotificationtCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'from_user', 'to_user', 'read', 'iSfollow', 'likedpost']
