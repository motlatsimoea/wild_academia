from django.contrib import admin
from .models import *

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)



