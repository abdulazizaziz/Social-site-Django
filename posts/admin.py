from django.contrib import admin

from .models import Post, Img, Comments
# Register your models here.


admin.site.register(Post)
admin.site.register(Img)
admin.site.register(Comments)