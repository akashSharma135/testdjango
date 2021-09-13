from .models import ManagerAssigned, NewUser
from django.contrib import admin

    
admin.site.register(NewUser)

@admin.register(ManagerAssigned)
class ManagerAssignedAdmin(admin.ModelAdmin):
    list_display = ['id', 'manager', 'user', 'task_id']
