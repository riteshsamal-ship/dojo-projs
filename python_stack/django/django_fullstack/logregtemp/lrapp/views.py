from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .models import Quote
# Create your views here.
def index(request):
    return render(request, 'index.html')

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
        return redirect('/quotes')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in!")
    return redirect('/quotes')

def logout(request):
    request.session.clear()
    return redirect('/')

def quotes(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'all_quotes': Quote.objects.all(),
        'this_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'quotes.html', context)

def create_quote(request):
    errors = Quote.objects.quote_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/quotes')
    else:
        user = User.objects.get(id=request.session['user_id'])
        quote = Quote.objects.create(
            poster = user,
            author = request.POST['author'],
            description = request.POST['description']
        )

    return redirect('/quotes')

def show_one(request, quote_id):
    quote = Quote.objects.get(id = quote_id)
    user = User.objects.get(id=quote.poster.id)
    
    context = {
        'all_quotes': Quote.objects.all(),
        'keyquote': quote,
        'poster': user
    }
    return render(request, "show_one.html", context)

def delete(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    quote.delete()

    return redirect('/quotes')

def edit(request):
    return render(request, 'edit.html')

def update(request):
    user = User.objects.get(id=request.session['user_id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/quotes')
