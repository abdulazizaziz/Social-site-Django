from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    post, postimgs, createpost, image,
    createpostimage, getpost, somepost,
    deletepost, addcomment, deletecomment,
    editcomment, addlike, removelike, updatepost,
    addsaved, removesaved, savedpost
)

router = DefaultRouter()
router.register('', createpost)

urlpatterns = [
    path('delete/<int:id>/', deletepost),
    path('getpost/<int:id>/', getpost),
    path('imgs/', postimgs),
    path('createimgs/', createpostimage.as_view()),
    path('create/', include(router.urls)),
    path('update/<int:id>/', updatepost),
    path('some/<str:username>/', somepost),
    path('<int:id>/', post),
    path('addcomment', addcomment),
    path('deletecomment/<int:id>/', deletecomment),
    path('editcomment/<int:id>/', editcomment),
    path('addlike/<int:id>/<int:postid>/', addlike),
    path('removelike/<int:id>/<int:postid>/', removelike),
    path('addsaved/<int:id>/<int:postid>/', addsaved),
    path('removesaved/<int:id>/<int:postid>/', removesaved),
    path('savedpost/<int:id>/', savedpost)
]