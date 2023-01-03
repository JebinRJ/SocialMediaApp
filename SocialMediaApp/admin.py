from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowerCount)

# Register your models here.
