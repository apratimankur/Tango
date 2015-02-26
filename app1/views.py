from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from app1.models import *
# Create your views here.


def index(request):
    return HttpResponse('Tango With Django...')


def ankur(request):
    context_dir = {
    	'person' : Person.objects.filter(name="ankur")[0],
    }
    return render_to_response('index.html', context_dir, context_instance=RequestContext(request))

@csrf_exempt
def register(request):
	try:
		name = request.POST['name']
	except:
		return HttpResponse('invalid name')
	try:
		email = request.POST['email']
	except:
		return HttpResponse('invalid email')
	try:
		location = request.POST['location']
	except:
		return HttpResponse('invalid location')
	try:
		contact_no = request.POST['contact_no']
	except:
		return HttpResponse('invalid contact_no')
	try:
		user = Person.objects.create(name=name,email=email,location=location,contact_no=contact_no)
	except:
		return HttpResponse('oops...please try again...')
	return HttpResponse('successfully_registered..Thank you '+str(user.name))