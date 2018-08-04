from django.shortcuts import render
import json
import os
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Context, Template
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User

# Templating
from django.template import loader

# Endpoints
from endpoints import endpoints

# Password hash
from .utility import hash_password, signup_validate

# Models
from .models import Faq, Testimonial

"""
|_______________________________________
|   Heathcheck|
|_______________________________________
"""
def healthcheck(request):
    text = 'Up and running'
    return HttpResponse(text)

"""
|_______________________________________
|   Home Page|
|_______________________________________
"""
# home page to see both FAQ and testimonial
def home(request):
    if request.method == 'GET':
        template = loader.get_template('home.html')
        testimonials = Testimonial.objects.all()
        faqs = Faq.objects.all()
        if request.user.is_authenticated: first_name = request.user.first_name
        else: first_name = None
        context = {
            'first_name': first_name,
            'testimonials': testimonials,
            'count': len(testimonials),
            'faqs': faqs,
            'endpoints': endpoints,
            }
        return HttpResponse(template.render(context, request))


"""
|_______________________________________
|   Account Management|
|_______________________________________
"""
# sign in
def signin(request):
    if request.method == 'GET':
        template = loader.get_template('signin.html')
        context = {'endpoints': endpoints,}
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        if user_id and password:
            password = hash_password(password)
            if user_id.endswith('.com'): # email
                try:
                    user_id = User.objects.get(email=user_id).username
                except:
                    return JsonResponse({'status': 'Email not exist'})
            user = authenticate(request, username = user_id, password = password)
            if user:
                login(request, user)
                return JsonResponse({'status': 'success', 'redirect_url': endpoints.home})
        return JsonResponse({'status': 'Login failed'})

# sign up
def signup(request):
    if request.method == 'GET':
        template = loader.get_template('signup.html')
        context = {'endpoints': endpoints}
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if signup_validate(phone, email, first_name, last_name, password, confirm_password):
            hashed_password = hash_password(password)
            try:
                # for the sake of simplexity, I did not create a customized user model in this homework, so for now I use username to store phone number
                user = User.objects.create_user(username=phone, email=email, password=hashed_password, first_name=first_name, last_name=last_name)
                login(request, user)
                return JsonResponse({'status': 'success', 'redirect_url': endpoints.home})
            except Exception as e:
                return JsonResponse({'status': str(e)})
        else:
            return JsonResponse({'status': 'Data validation failed'})

# sign out
def signout(request):
    logout(request)
    return redirect(home)


"""
|_______________________________________
|   FAQ and Testimonial Management|
|_______________________________________
"""
# add frequently asked question
@login_required
def add_faq(request):
    if request.method == 'GET':
        template = loader.get_template('add_faq.html')
        context = {'endpoints': endpoints}
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        question = request.POST['question']
        answer = request.POST['answer']
        if question and answer:
            try:
                faq = Faq.objects.create(question=question, answer=answer)
                faq.save()
                return JsonResponse({'status': 'success', 'redirect_url': endpoints.home})
            except Exception as e:
                return JsonResponse({'status': str(e)})
        return JsonResponse({'status': 'missing question or answer'})

# add testimonial
@login_required
def add_testimonial(request):
    if request.method == 'GET':
        template = loader.get_template('add_testimonial.html')
        context = {'endpoints': endpoints}
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        styling_goal = request.POST['styling_goal']
        testimonial = request.POST['testimonial']
        if styling_goal and testimonial:
            try:
                testimonial = Testimonial.objects.create(styling_goal=styling_goal, testimonial=testimonial)
                testimonial.save()
                return JsonResponse({'status': 'success', 'redirect_url': endpoints.home})
            except Exception as e:
                return JsonResponse({'status': str(e)})
        return JsonResponse({'status': 'missing styling goal or testimonial'})

"""
|_________________________________________________________
|   Index to check mobile site for the front-end homework|
|_________________________________________________________
"""

def index(request):
    if request.method == 'GET':
        template = loader.get_template('index.html')
        return HttpResponse(template.render(None, request))