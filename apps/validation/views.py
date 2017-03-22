from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.forms.models import model_to_dict
from models import User
# Create your views here.
'''Landing page w/ 2 forms (login and registration)'''
def index(request):
    return render(request, 'validation/index.html')

'''Call method to creat a new user or login user and enter session'''
def validateUser(request, route):
    if request.method == 'POST':
        if route == 'reg':
            newUser = User.objects.newUser(request.POST)
        else:
            newUser = User.objects.validateUser(request.POST)
        # print '-' * 80
        # print 'newUser',newUser
        if not newUser[1]:
            for x in range(len(newUser[0])):
                messages.error(request, newUser[0][x])
            return redirect(reverse('login:login'))
        else:
            request.session['user'] = model_to_dict(newUser[0])
            return redirect(reverse('secret:home'))
    else:
        return redirect(reverse('login:login'))

'''Call method to exit session'''
def logOut (request):
    request.session.clear()
    return redirect(reverse('login:login'))
