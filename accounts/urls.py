from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework.routers import DefaultRouter

from .views import (
    UserApi, Token, UsernameCheck,
    showuser, getuser, show, showuserid,
    getfollowing, getfollower, removefollow,
    addfollow, Editaccount, usernameuniqe,
    emailuniqe, topuser, NotiPost, notification
)

router = DefaultRouter()
router.register('edit', Editaccount)
router.register('notification', NotiPost)



urlpatterns = [
    path('', include(router.urls)),
    path('noti/<int:id>/', notification),
    path('topuser/', topuser),
    path('createuser/', UserApi.as_view()),
    path('token/', Token.as_view()),
    path('tokenV/', TokenVerifyView.as_view()),
    path('check/', UsernameCheck.as_view()),
    path('showuser/<str:username>/', showuser),
    path('showuserid/<int:id>/', showuserid),
    path('getuser/<int:id>/', getuser),
    path('getfollowing/<int:id>/', getfollowing),
    path('getfollower/<int:id>/', getfollower),
    path('addfollow/<int:id>/<int:add>/', addfollow),
    path('removefollow/<int:id>/<int:remove>/', removefollow),
    path('usernameuniqe/<str:username>/', usernameuniqe),
    path('emailuniqe/<str:email>/', emailuniqe),
    path('show/', show)
]