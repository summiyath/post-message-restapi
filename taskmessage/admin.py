from django.contrib import admin

# Register your models here.
from taskmessage.models import Message
from django.contrib.auth.models import User

admin.site.register(Message)
