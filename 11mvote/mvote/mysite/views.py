#-*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from allauth.account.decorators import verified_email_required
from mysite import models

# Create your views here.
####
#   原始還沒有分類功能時的index，只顯示所有商品
####
# def index(request):
#     all_products = models.Product.objects.all()
#     paginator = Paginator(all_products, 5)
#     p = request.GET.get('p')

#     try:
#         products = paginator.page(p)
#     except PageNotAnInteger:
#         products = paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)  #如果頁面不存在（例如輸入的頁碼超過實際頁碼），則顯示最後一頁的內容。

#     return render(request, 'index.html', locals())



def index(request, id=0):
    """
    Displays all products if id is 0, otherwise displays products of specified category id.

    :param request: the request object
    :param id: the category id, defaults to 0
    :return: the rendered index.html page
    """
    try:
        all_products = None
        all_categories = models.Category.objects.all()
        # cart = Cart(request).cart

        if id > 0:
            category = models.Category.objects.get(id=id)
            if category is not None:
                all_products = models.Product.objects.filter(category=category)

        if all_products is None:
            all_products = models.Product.objects.all()

        paginator = Paginator(all_products, 5)

        p = request.GET.get('p')

        products = paginator.page(p)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    except Exception:
        products = []

    return render(request, 'index.html', locals())

def product(request, id):   # id是product的id，不處理id=0，也不處理不存在的id，一律返回None
    try:
        product = models.Product.objects.get(id=id)
    except:
        product = None

    return render(request, 'product.html', locals())


@login_required
# @verified_email_required
def poll(request, pollid):
    try:
        poll = models.Poll.objects.get(id = pollid)
    except:
        poll = None
    if poll is not None:
        pollitems = models.PollItem.objects.filter(poll=poll).order_by('-vote')
    return render(request, 'poll.html', locals())

# @login_required
# def vote(request, pollid, pollitemid):
#     try:
#         pollitem = models.PollItem.objects.get(id = pollitemid)
#     except:
#         pollitem = None
#     if pollitem is not None:
#         pollitem.vote = pollitem.vote + 1
#         pollitem.save()
#     target_url = '/poll/{}'.format( pollid)
#     return redirect(target_url)

@login_required
def vote(request, pollid, pollitemid):
    target_url = '/poll/{}'.format( pollid)

    try:
        if models.VoteCheck.objects.filter(userid=request.user.id, pollid=pollid, vote_date = datetime.date.today()):
            return redirect(target_url)

        vote_rec = models.VoteCheck(userid=request.user.id, pollid=pollid, vote_date = datetime.date.today())
        vote_rec.save()

        pollitem = models.PollItem.objects.get(id = pollitemid)

        if pollitem is not None:
            pollitem.vote = pollitem.vote + 1
            pollitem.save()
    except:
        pollitem = None

    return redirect(target_url)

@login_required
def govote(request):
    try:
        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

        votes = 0

        if (request.method != "GET") or (not is_ajax):
            return HttpResponse(votes)

        pollid = request.GET.get('pollid')
        is_voted = models.VoteCheck.objects.filter(userid=request.user.id, pollid=pollid, vote_date = datetime.date.today())

        if (not is_voted):
            pollitemid = request.GET.get('pollitemid')
            pollitem = models.PollItem.objects.get(id=pollitemid)
            pollitem.vote = pollitem.vote + 1
            pollitem.save()
            votes = pollitem.vote

            vote_rec = models.VoteCheck(userid=request.user.id, pollid=pollid, vote_date = datetime.date.today())
            vote_rec.save()

        return HttpResponse(votes)
    except:
        votes = 0
        return HttpResponse(votes)


