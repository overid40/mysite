from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from board.models import Board


def index(request):
    board_list = Board.objects.all().order_by('-id')

    context = {'board_list': board_list}
    return render(request, 'board/list.html', context)


def modifyform(request):
    # 인증 체크
    if request.session.get('authuser') is None:
        return HttpResponseRedirect('/user/loginform')

    board_id = request.GET['id']

    context = {'board_id': board_id}
    return render(request, 'board/modify.html', context)


def modify(request):
    # 인증 체크
    if request.session.get('authuser') is None:
        return HttpResponseRedirect('/user/loginform')

    board = Board.objects.all().get(id=request.POST['no'])
    board.title = request.POST['title']
    board.content = request.POST['content']

    board.save()

    return HttpResponseRedirect('/board')


def viewform(request):
    # 인증 체크
    if request.session.get('authuser') is None:
        return HttpResponseRedirect('/user/loginform')

    board_list = Board.objects.all().filter(id=request.GET['id'])

    context = {'board_list': board_list}
    return render(request, 'board/view.html', context)


def writeform(request):
    # 인증 체크
    if request.session.get('authuser') is None:
        return HttpResponseRedirect('/user/loginform')

    return render(request, 'board/write.html')


def write(request):
    # 인증 체크
    if request.session.get('authuser') is None:
        return HttpResponseRedirect('/user/loginform')

    board = Board()
    board.title = request.POST['title']
    board.content = request.POST['content']
    board.user_id = request.session['authuser']['id']

    board.save()

    return HttpResponseRedirect('/board')


def delete(request):
    # 인증 체크
    if request.session.get('authuser') is None:
        return HttpResponseRedirect('/user/loginform')

    Board.objects.filter(id=request.GET['id']).delete()

    return HttpResponseRedirect('/board')
