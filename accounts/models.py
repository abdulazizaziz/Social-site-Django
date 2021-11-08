from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

from django.contrib.auth.hashers import make_password
from django.utils.timesince import timesince



# Create your models here.

GENDER = [
    ('male', 'Male'),
    ('female', 'Female')
]
IsSingle = [
    ('single', 'Single'),
    ('married', 'Married')
]



class AccountManager(BaseUserManager):
    def simplecreate(self, email, username, name, gender, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError("User must have an Email")

        user = self.model(email=email, name=name)
        user.set_password(password)
        user.username = username
        user.gender = gender
        user.img = 'noimg.png'
        user.save(using=self._db)
        return user
    def create_user(self, email, username, name, gender, birth, country, education, live_city, live_country, img, about, password=None, single=None):
        """ Create a new user profile """
        if not email:
            raise ValueError("User must have an Email")

        user = self.model(email=email, name=name)
        user.set_password(password)
        user.gender = gender
        user.username = username
        user.birth = birth
        user.country = country
        user.education = education
        user.live_city = live_city
        user.live_country = live_country
        user.img = img
        user.single = single
        user.about = about
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, gender='male', password=None):
        """ Create and save superuser """

        if not email:
            raise ValueError("User must have email")

        user = self.model(email=email, name=name)

        user.set_password(password)
        user.gender = gender
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=50, choices=GENDER)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    birth =  models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    live_city = models.CharField(max_length=100, null=True, blank=True)
    live_country = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    number = models.BigIntegerField(null=True, blank=True)
    single = models.CharField(max_length=50 ,null=True, blank=True, choices=IsSingle)
    about = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True, null=True, blank=True)

    following = models.ManyToManyField("Account", null=True, blank=True, related_name="follow")
    likes = models.ManyToManyField("posts.Post", null=True, blank=True, related_name="postlikes")
    saved = models.ManyToManyField("posts.Post", null=True, blank=True, related_name="postsaved")
    



    @property
    def age(self):
        if self.birth:
            age = timesince(self.birth)
            index = age.find(',')
            if index != -1:
                age = age[:index]
            return age
        return ''

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gender', 'name']

    objects = AccountManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.following.add(self.id)

    class Meta:
        db_table = 'account'
        verbose_name = "account"
        verbose_name_plural = "accounts"

    def __str__(self):
        return self.name


class Notification(models.Model):
    from_user = models.ForeignKey("Account", on_delete=models.CASCADE, related_name='To')
    to_user = models.ForeignKey("Account", on_delete=models.CASCADE, related_name='notification')
    read = models.BooleanField(default=False)
    iSfollow = models.BooleanField(default=False)
    likedpost = models.ForeignKey("posts.Post", null=True, blank=True, on_delete=models.CASCADE)