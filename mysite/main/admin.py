from django.contrib import admin
from .models import AccessRequest


class AccessRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    readonly_fields = ('password',)
    search_fields = ('email',)


admin.site.register(AccessRequest, AccessRequestAdmin)
