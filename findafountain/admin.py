from django.contrib import admin
from findafountain.models import UserProfile, Fountain, Review, Rating

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('id',)}

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Fountain)
admin.site.register(Review)
admin.site.register(Rating)
