from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from models import Applicant

# Create your views here.
def home(request):
	"""Home page"""
    
	return render(request, '/home.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def register(request):

	"""Register as an Applicant."""

	if request.method == 'POST':
		user_info = request.POST
		valid_user = True

		email = user_info.get('email',None)
        if not email:
        	error = "Input email is missing"
        	messages.add_message(request, messages.ERROR, error)
        	return render(request, 'portal/home.html')

		if Applicant.objects.filter(email = user_info['email']).exists():
			valid_user = False
			error = 'This email is already registered.'
			logger.error(error + user_info['email'])
			messages.add_message(request, messages.ERROR, error)

		if Applicant.objects.filter(phone = user_info['phone']).exists():
			valid_user = False
			error = 'This phone number is already registered.'
			logger.error(error + user_info['phone'])
			messages.add_message(request, messages.ERROR, error)

		if not valid_user:
			return render(request, 'portal/home.html')

		request.session['first_name'] = user_info['first_name']
		request.session['last_name'] = user_info['last_name']
		request.session['email'] = user_info['email']
		request.session['phone'] = user_info['phone']
		request.session['city'] = user_info['city']
		request.session['state'] = user_info['state']
		request.session['zipcode'] = user_info['zipcode']
		request.session['email'] = user_info['email']

		return render(request, 'portal/background_check.html')


def confirm_registration(request):
	"""Saves user credentials from request.session"""

	email = request.session['email']
	if request.method == 'POST':
		applicant = Applicant.objects.filter(email=email)

		if applicant:
			context = RequestContext(request, {'applicant':applicant})
			return render(request, 'portal/confirm_registration.html')


		first_name = request.session['first_name']
		last_name = request.session['last_name']
		email = request.session['email']
		phone = request.session['phone']
		city = request.session['city']
		state = request.session['state']
		zipcode = request.session['zipcode']

		applicant = Applicant(first_name=first_name, last_name=last_name, email=email,
						phone=phone, city=city, state=state, zipcode=zipcode)

		applicant.save()

		context = RequestContext(request, {'applicant':applicant})

		
        del request.session['first_name']
        del request.session['last_name']
        del request.session['phone']
        del request.session['city']
        del request.session['state']
        del request.session['zipcode']

    	logger.info("New applicant registered. Email: %s", email)
    
    	return render(request, '/portal/confirm_registration.html', context)


def edit_application(request):

	"""Allows applicant to edit the application."""

	applicant = Applicant.objects.filter(email=request.session['email'])
	context = RequestContext(request, {'applicant':applicant[0]})
	return render(request, 'portal/edit_application.html', context)

def update_application(request):

	"""Updates an applicant's credentials."""

	applicant = Applicant.objects.filter(email=request.session['email'])[0]
	
	phone = request.POST['phone']

	if applicant.phone != int(phone) and Applicant.objects.filter(phone=int(phone)).exists():
		error = 'Phone number already exists.'
		logger.error(error)
		messages.add_message(request, messages.ERROR, error)
		context = RequestContext(request, {'applicant':applicant})
		return render(request, 'portal/edit_application.html', context)

	applicant.first_name = request.POST['first_name']
	applicant.last_name = request.POST['last_name']
	applicant.phone = request.POST['phone']
	applicant.city = request.POST['city']
	applicant.state = request.POST['state']
	applicant.zipcode = request.POST['zipcode']
	applicant.save()

	email = request.session['email']
	message = "Application updated for " + email
	messages.info(request, message)
	context = RequestContext(request, {'applicant':applicant})
	return render(request, '/login.html', context)



def login(request):

	"""Allows a user to login."""


	if request.method =='POST':
		email = False
		try:
		    email = request.POST['email']
		except:
			pass

		print email

		if not email:
			error = 'Please login with a valid email.'
			logger.error(error)
			messages.add_message(request, messages.ERROR, error)
			return render(request, 'portal/home.html')

		if Applicant.objects.filter(email=email).exists():
			request.session['email'] = email
			applicant = Applicant.objects.filter(email=email)[0]
			context = RequestContext(request, {'applicant':applicant})
			return render(request, 'portal/login.html', context)
		else:
			error = 'No applicant found with this email:' + email
			logger.error(error)
			messages.add_message(request, messages.ERROR, error)
			return render(request, 'portal/home.html')


def logout(request):
    try:
        del request.session['email']
    except Exception as e:
        logger.error("Failed to delete session variable. Email: %s,  Reason:%s", request.session['email'], str(e))
        
    return render(request, 'portal/home.html')




