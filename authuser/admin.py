from django.contrib import admin

# Register your models here.
from .models import User

@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    readonly_fields = ('rmg_to_reg', 'login_to_reg')