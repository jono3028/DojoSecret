from django.shortcuts import render, redirect, reverse
from .models import Secret
# Create your views here.
def index(request):
    try:
        request.session['user']
    except KeyError:
        return redirect(reverse('login:login'))
    context = {
        'posts': Secret.objects.getSecrets()
    }
    print '-' * 80
    print Secret.objects.filter(likes=request.session['user']['id'])
    return render(request, 'dojo_secret/index.html', context)
    # if request.session['user']:
    # else:

'''calls method to make a secret in DB '''
def postSecret(request):
    if request.POST['secret']:
        Secret.objects.makeSecret(request.POST)
        return redirect('secret:home')
    else:
        return redirect('secret:home')

'''calls method to remove from DB'''
def deleteSecret(request, post_id):
    Secret.objects.deleteSecret(post_id)
    return redirect('secret:home')

'''calls method to like a secret'''
def likeSecret(request, post_id):
    Secret.objects.likeSecret(request.session['user']['id'], post_id)
    return redirect('secret:home')

'''renders page displaying most popular secrets'''
def mostPopular(request):
    try:
        request.session['user']
    except KeyError:
        return redirect(reverse('login:login'))
    context = {
        'posts': Secret.objects.getPopular()
    }
    return render(request, 'dojo_secret/popular.html', context)
