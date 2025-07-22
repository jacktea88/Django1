from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    post_list = list()

    for count, post in enumerate(posts):
        post_list.append(f"Post {count}: {post} <br> {post.body} <br>")
        # print(post)

    poems = [
        {'content': '床前明月光，疑是地上霜。舉頭望明月，低頭思故鄉。', 'title_author': '李白 - 靜夜思'},
        {'content': '國破山河在，城春草木深。感時花濺淚，恨別鳥驚心。', 'title_author': '杜甫 - 春望'},
        {'content': '白日依山盡，黃河入海流。欲窮千里目，更上一層樓。', 'title_author': '王之涣 - 登鸛雀樓'},
        {'content': '春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。', 'title_author': '孟浩然 - 春曉'},
        {'content': '空山不見人，但聞人語響。返景入深林，復照青苔上。', 'title_author': '王維 - 鹿柴'},
        {'content': '兩岸猿聲啼不住，light風回雪晚。青山相接處，行人跡難半。', 'title_author': '李白 - 江上吟'},
        {'content': '明月出天山，苔痕上架。疑是地上霜，舉頭望明月。', 'title_author': '李白 - 蜀道難'},
        {'content': '憶江南，憶江南，憶江南。春衫著起，憶江南。', 'title_author': '白居易 -憶江南'},
        {'content': '君不見黃河之水天上來，奔流到海不復回。君不見高堂明鏡悲白髮，早生華髮人生幾何。', 'title_author': '李白 -將進酒'},
        {'content': '床前明月光，疑是地上霜。舉頭望明月，低頭思故鄉。', 'title_author': '李白 -靜夜思'},
    ]
    # return HttpResponse("Hello World!")
    # return HttpResponse(post_list)
    
    # return render(request, 'homepage.html', {'posts': Post.objects.all()})
    return render(request, 'index.html', locals())

def showpost(request, slug):
    post = Post.objects.get(slug=slug) #(欄位名稱=傳進來的變數值)
    return render(request, 'post.html', locals())

