from django.contrib import admin

# Register your models here.
from .models import Listing,LikedListing

class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

admin.site.register(Listing,ListingAdmin)

class LikeListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

admin.site.register(LikedListing,LikeListingAdmin)
