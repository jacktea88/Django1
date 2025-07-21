from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    post_list = list()
    for count, post in enumerate(posts):
        post_list.append(f"Post {count}: {post} <br> {post.body} <br>")
        print(post)
    # return HttpResponse("Hello World!")
    # return HttpResponse(post_list)
    
    # return render(request, 'homepage.html', {'posts': Post.objects.all()})
    return render(request, 'index.html', locals())