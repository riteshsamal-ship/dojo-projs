from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .models import Wish
# Create your views here.
def index(request):
    return render(request, 'index.ml')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/dash')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in!")
    return redirect('/dash')

def logout(request):
    request.session.clear()
    return redirect('/')

def dash(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'granted_wishes': user.wish.all().filter(granted=true)
       # Wish.objects.d
    }
    return render(request, 'dash.html', context)

def create_wish(request, id):
    errors = Wish.objects.wish_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/mwish')
    else:
        user = User.objects.get(id=request.session["id"])
        user_wish = Wish.objects.create(
            wish = request.POST['wish'],
            description = request.POST['description'],
            creator = user
        )
        # bonus: the book creator automatically favorites the book
        user.wish.add(wish)

        return redirect(f'/dash/{wish.id}')