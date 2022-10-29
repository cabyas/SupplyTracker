from django.contrib import admin

from tracker.models import Network, SupplySnapshot, Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code_name', 'contract_address')
    list_display = ('name', 'code_name', 'contract_address')
    list_filter = ('name', )


@admin.register(SupplySnapshot)
class SupplySnapshotAdmin(admin.ModelAdmin):
    search_fields = ('token', )
    list_display = ('token', 'created_at', 'supply')
    list_filter = ('token', )


admin.site.register(Network)
