from django.contrib import admin
from .models import Item, User, Feedback
# Register your models here.

admin.site.register(Item)
admin.site.register(User)
admin.site.register(Feedback)