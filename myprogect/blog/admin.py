from django.contrib import admin
from .models import Blog, Profile, Tag

admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(Tag)