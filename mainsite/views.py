#-*- coding: utf-8 -*-
from django.shortcuts import redirect
from datetime import datetime
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


def homepage(request):
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 3) # 每页显示3条
    page = request.GET.get('page')
    now = datetime.now()
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页。
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'contacts': contacts, 'now': now})



def showpost(request, id):
    try:
        post = Post.objects.get(id=id)
        if post != None:
            return render(request, 'post.html', {'post': post})
    except:
        return redirect('/')