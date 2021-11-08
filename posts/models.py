from django.db import models
from django.utils.timesince import timesince

from accounts.models import Account

import os
# Create your models here.



class Post(models.Model):
    user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE)
    article = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    @property
    def added_on(self):
        ago = timesince(self.time)
        index = ago.find(',')
        if index != -1:
            ago = ago[:index]
        return ago


    class Meta:
        db_table = "Post"
        ordering = ['-time']
    def __str__(self):
        return str(self.id)
    


class Img(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="imgs")
    img = models.ImageField()
        
    def delete(self):
        os.remove(f'media/{self.img}')
        super().delete()

    class Meta:
        db_table = "Img"
    def __str__(self):
        return self.post.user.name
    
    
class image(models.Model):
    img = models.ImageField()


class Comments(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name="comment")
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    @property
    def added_on(self):
        ago = timesince(self.time)
        index = ago.find(',')
        if index != -1:
            ago = ago[:index]
        return ago

    class Meta:
        db_table = "Comment"
        ordering = ['-time']
    def __str__(self):
        return str(self.id)