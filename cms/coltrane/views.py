from django.shortcuts import render_to_response
from coltrane.models import Entry
from django.shortcuts import get_object_or_404

def entries_index(request):
	return render_to_response('coltrane/entry_index.html',
								{'entry_list':Entry.objects.all()})



def entry_details(request,year,moth,day,slug):
	import datetime,time
	date_stamp = time.strptime(year+month+day,"%Y%b%d")
	pub_date = datetime.date(*date_stamp[:3])
	entry=get_object_or_404(Entry,pub_date__year=pub_date.year,
									pub_date__month=pub_date.month,
									pub_date__day=pub_date.day,
									slug=slug)

	return render_to_response('coltrane/entry_details.html',
								{'entry':entry })


	"""return render_to_response('coltrane/entry_details.html',
								{'entry':Entry.objects.get(pub_date__year=pub_date.year,
									pub_date__month=pub_date.month,
									pub_date__day=pub_date.day,
									slug=slug) })"""

