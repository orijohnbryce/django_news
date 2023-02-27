from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import Permission
from .models import Post

admin.site.register(Post)
admin.site.register(Permission)
