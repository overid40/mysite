from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from guestbook.models import Guestbook

# Create your views here.
from user.models import User


def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')

    context = {'guestbook_list': guestbook_list}
    return render(request, 'guestbook/list.html', context)


def deleteform(request):
    guestbook_id = request.GET['id']

    context = {'guestbook_id': guestbook_id}
    return render(request, 'guestbook/deleteform.html', context)


def delete(request):
    Guestbook.objects.filter(id=request.POST['no']).filter(password=request.POST['password']).delete()
    return HttpResponseRedirect('/guestbook')


def add(request):
    if (request.session['authuser']['name'] == request.POST['name']) and (request.session['authuser']['password'] == request.POST['pass']):
        guestbook = Guestbook()
        guestbook.name = request.POST['name']
        guestbook.password = request.POST['pass']
        guestbook.message = request.POST['content']

        guestbook.save()

    return HttpResponseRedirect('/guestbook')



