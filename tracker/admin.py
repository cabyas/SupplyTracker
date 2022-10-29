from django.contrib import admin

from tracker.models import Network, SupplySnapshot, Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code_name', 'contract_address')
    list_display = ('name', 'code_name', 'contract_address')
    list_filter = ('name', )
    actions = ('create_supply_record', )

    @admin.action(description="Create supply record")
    def create_supply_record(self, request, queryset):
        for token in queryset:
            token.create_supply_snapshot()


@admin.register(SupplySnapshot)
class SupplySnapshotAdmin(admin.ModelAdmin):
    search_fields = ('token', )
    list_display = ('token', 'created_at', 'supply')
    list_filter = ('token', )


admin.site.register(Network)
