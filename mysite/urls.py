"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import main.views as main_views
import guestbook.views as guestbook_views
import board.views as board_views
import user.views as user_view

urlpatterns = [
    path('board/', board_views.index),
    path('board/modifyform', board_views.modifyform),
    path('board/modify', board_views.modify),
    path('board/viewform', board_views.viewform),
    path('board/writeform', board_views.writeform),
    path('board/write', board_views.write),
    path('board/delete', board_views.delete),

    path('guestbook/', guestbook_views.index),
    path('guestbook/add', guestbook_views.add),
    path('guestbook/deleteform', guestbook_views.deleteform),
    path('guestbook/delete', guestbook_views.delete),

    path('', main_views.index),

    path('user/joinform/', user_view.joinform),
    path('user/join', user_view.join),
    path('user/joinsuccess/', user_view.joinsuccess),
    path('user/loginform/', user_view.loginform),
    path('user/login', user_view.login),
    path('user/logout', user_view.logout),

    path('admin/', admin.site.urls),
]
