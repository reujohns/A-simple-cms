from django.contrib import admin
from coltrane.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
	#pass
	prepopulated_fields = {'slug':['title']}


class EntryAdmin(admin.ModelAdmin):
	#pass
	prepopulated_fields = {'slug':['title']}

				
admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)

	