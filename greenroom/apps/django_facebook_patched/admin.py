from django.contrib import admin
from greenroom.apps.django_facebook_patched import models


class FacebookUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'facebook_id',)
    search_fields = ('name',)


class FacebookLikeAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'category', 'facebook_id',)
    search_fields = ('name',)
    filter_fields = ('category', )


admin.site.register(models.FacebookUser, FacebookUserAdmin)
admin.site.register(models.FacebookLike, FacebookLikeAdmin)
