from django.contrib import admin
from .models import Post, Breaking, Tv, Series

admin.site.register(Post)
admin.site.register(Tv)
admin.site.register(Breaking)
admin.site.register(Series)

