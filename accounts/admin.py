from django.contrib import admin

from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(UserAdmin):
    list_display = ('username', 'group', 'date_joined', 'last_login', 'is_staff')
    search_fields = ('username', 'group')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(MyUser)
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(Township)
admin.site.register(District)



