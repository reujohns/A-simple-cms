from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader, Context
from django.contrib.flatpages.models import FlatPage 
from django.views.generic import View
from django.shortcuts import render

from django.shortcuts import render_to_response

# Create your views here.

def search(request):
	query = request.GET.get('q','')
	"""results = FlatPage.objects.filter(content__icontains=query)
	template = loader.get_template('search/search.html')
	context = Context({'query':query,'results':results })
	response = template.render(context)

	return HttpResponse(response)"""
	"""return render_to_response('search/search.html',
								{'query': query,
								'results':FlatPage.objects.filter(content__icontains=query)})"""

	keyword_results = results = []
	if query:
		keyword_results = FlatPage.objects.filter(
			searchkeyword__keyword__in=query.split()).distinct()
		if keyword_results.count()==1:
			return HttpResponseRedirect(keyword_results[0].get_absolute_url())
		results = FlatPage.objects.filter(content__icontains=query)
			
	return render_to_response('search/search.html',
							{	'query':query,
								'keyword_results':keyword_results,
								'results':results })	

class Index(View):
	def get(self,request):
		#pages={}
		return render(request,'flatpages/index.html')