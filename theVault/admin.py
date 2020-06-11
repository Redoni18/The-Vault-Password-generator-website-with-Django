from django.contrib import admin
from .models import NewPassword, Profile, NewNote
# Register your models here.

admin.site.register(NewPassword)
admin.site.register(NewNote)
admin.site.register(Profile)