from django.contrib import admin
from Accounts.models  import User





@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ["id","username","first_name","last_name","email","is_staff","is_active"]