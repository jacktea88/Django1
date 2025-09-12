from django.shortcuts import render, redirect
from mysite import models

# Create your views here.
# def index(request):
#     years = range(1912, 2020)
#     try:
#         user_id = request.GET['user_id']
#         user_pass = request.GET['user_pass']
#         user_byear = request.GET['byear']
#         urfcolor = request.GET.getlist('fcolor')
#         # user_post = request.GET['user_post']
#         # user_mood = request.GET['mood']
#     except:
#         user_id = None
#     if user_id == 'admin' and user_pass == '12345678':
#         verified = True
#     else:
#         verified = False
#     # print(user_id, verified)    
#     print(user_id, user_pass, verified, user_byear, urfcolor)    
#     return render(request, 'index.html', locals())

def index(request):
    posts = models.Post.objects.all().order_by('-pub_time')
    moods = models.Mood.objects.all()
    try:
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
        # user_id = request.GET['user_id']
        # user_pass = request.GET['user_pass']
        # user_post = request.GET['user_post']
        # user_mood = request.GET['mood']

    except:
        user_id = None
        message = '每一欄都要填寫'
    if user_id != None:
        mood = models.Mood.objects.get(status = user_mood)
        post = models.Post(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass)
        post.save()
        message = '張貼成功'
    else:
        message = '無效的帳號'
    # print(user_id, user_pass, user_post, user_mood)    
    return render(request, 'index_post.html', locals())

def delpost(request, post_id=None, del_pass=None):
    if del_pass and post_id:
        try:
            post = models.Post.objects.get(id = post_id)
            if post.del_pass == del_pass:
                post.delete()
                message = '刪除成功'
                print('刪除成功')
            else:
                message = '密碼錯誤'
                print('密碼錯誤')
        except:
            message = '找不到貼文'
            print('找不到貼文')
    return redirect('/')
    