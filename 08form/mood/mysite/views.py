from django.shortcuts import render, redirect
from mysite import models, forms
from django.core.mail import EmailMessage
from django.conf import settings


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

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
            messages = '您的意見已傳送給我們'
            print(messages)
            mail_body = '姓名: %s\n城市: %s\n是否在學: %s\n電子郵件: %s\n意見: %s' % (user_name, user_city, user_school, user_email, user_message)
            email = EmailMessage('來自網站的意見', mail_body, settings.EMAIL_HOST_USER, [user_email])
            email.send()
            # print(settings.EMAIL_HOST_USER)
        else:
            messages = '請檢查您的輸入'
            print(messages)
    else:   # GET
        form = forms.ContactForm()
    return render(request, 'contact.html', locals())