from django.contrib import admin

from .models import User, Role, UserRole, Templates, Others


class RoleInlineAdmin(admin.TabularInline):
    model = UserRole
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'email', 'confirmed', 'mail_subscribe')
    list_filter = ('confirmed', 'mail_subscribe')
    search_fields = ('login', 'email',)
    fields = (
        'login',
        'email',
        'confirmed',
        'mail_subscribe',
        'password',
    )
    inlines = (RoleInlineAdmin,)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fields = (
        'name',
    )


@admin.register(Templates)
class TemplatesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fields = (
        'name',
        'template',
    )


@admin.register(Others)
class OthersAdmin(admin.ModelAdmin):
    list_display = ('title', 'template')
    search_fields = ('title',)
    fields = (
        'title',
        'description',
        'template',
    )