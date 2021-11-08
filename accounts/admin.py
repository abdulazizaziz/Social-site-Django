from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from accounts.models import Account, Notification
# Register your models here.


class AccountAdmin(BaseUserAdmin):
    fieldsets = [
        ("Personal Info", {"fields": ["email", 'password', 'gender',
         'name', 'username','birth', 'country', 'education', 'live_city', 'live_country',
          'img', 'number', 'single', 'about', 'following', 'likes', 'saved',
           'is_superuser', 'is_active', 'is_staff']}
           ),
        ("User Permission", {'fields': ["user_permissions"]})
    ]

    add_fieldsets = [
        (None, {"fields": [
            "email", 'gender', 'name', 'username', "password1",
            "password2",
        ]})
    ]
    list_display = ["id", "name", "email", "gender"]
    ordering = ['name']


# admin.site.unregister(User)
admin.site.register(Account, AccountAdmin)
admin.site.register(Notification)
