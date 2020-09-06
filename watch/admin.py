from django.contrib import admin
from .models import CommentLike,Comments,Videos,profile,Category,Reply
# Register your models here.
admin.site.register(Comments)
admin.site.register(CommentLike)
admin.site.register(Videos)
admin.site.register(profile)
admin.site.register(Category)
admin.site.register(Reply)
