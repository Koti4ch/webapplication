from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from django.conf import settings
from .models import PersonalUserInfo, User



# @admin.register(User)
# class UserAdminModel(admin.ModelAdmin):
    # readonly_fields = ('rmg_to_reg', 'login_to_reg')

class UserInfoInline(admin.StackedInline):
    model = PersonalUserInfo
    can_delete = False
    verbose_name_plural = 'Personal info'

    fields = ()
    list_display = ('radio_chanal',)

@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    inlines = [UserInfoInline,]
    readonly_fields = ('rmg_to_reg', 'login_to_reg')

    fields = ()
    list_display = ('username', 'radio_chanal_list', 'is_active')

    # 
    def radio_chanal_list(self, obj):
        shortname = obj.personaluserinfo.radio_chanal
        return obj.personaluserinfo.find_choice(shortname)
    radio_chanal_list.short_description = 'Radio chanal'

# admin.site.unregister(settings.AUTH_USER_MODEL)
# admin.site.register(settings.AUTH_USER_MODEL, UserAdminModel)