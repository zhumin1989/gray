from django.contrib import admin
from .models import User,Log,Treasure,Quest,Img,Sign
from django.contrib.admin.utils import model_ngettext
from django.contrib import messages
from django.utils.translation import gettext as _, gettext_lazy
# Register your models here.
# admin.site.register(User)
admin.site.register(Log)

admin.site.register(Quest)

admin.site.register(Sign)


def make_state_change(modeladmin, request, queryset):
    queryset.update(flag=True)
    admin.ModelAdmin.message_user(request, "Successfully changed.", messages.SUCCESS)
make_state_change.short_description = ''

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'img_data')
    readonly_fields = ('img_data',)


admin.site.register(Img,ProductAdmin)


class TreasureAdmin(admin.ModelAdmin):
    ordering = ['title']
    readonly_fields = ('img_data',)
    actions = ['make_state',make_state_change]

    def make_state(self,request, queryset):
            queryset.update(stat=2)
            self.message_user(request, "Successfully changed.", messages.SUCCESS)
    make_state.short_description = '宝物状态'
admin.site.register(Treasure,TreasureAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','currency')
admin.site.register(User,UserAdmin)