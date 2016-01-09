from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from search.models import SearchKeyword

# Register your models here.

class SearchKeywordInline(admin.StackedInline):
	#pass
	model = SearchKeyword

class  FlatPageAdminWithKeywords(FlatPageAdmin):
		inlines = [SearchKeywordInline]	

				


#admin.site.register(SearchKeyword, SearchKeywordAdmin)	
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)