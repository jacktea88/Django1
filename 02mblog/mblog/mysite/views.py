
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from mysite.models import Post, Product
from django.urls import reverse


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
    import random
    today_poem = random.choice(poems)
    print(today_poem)
    #
    #  return HttpResponse("Hello World!")
    # return HttpResponse(post_list)
    
    # return render(request, 'homepage.html', {'posts': Post.objects.all()})
    return render(request, 'index.html', locals())

def showpost(request, slug):
    post = Post.objects.get(slug=slug) #(欄位名稱=傳進來的變數值)
    return render(request, 'post.html', locals())


def listing(request):
    products = Product.objects.all()
    return render(request, 'listing.html', locals())

def listing2(request):
    html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>list products</title>
</head>
<body>
    <table class="table table-bordered" bgcolor="lightblue" border="1">
        {}
    </table>
</body>
</html>
'''
    products = Product.objects.all()
    tags = "<tr><td>name</td><td>price</td><td>qty</td></tr>"
    for product in products:
        tags += f"<tr><td>{product.name}</td><td>{product.price}</td><td>{product.qty}</td></tr>"
    html = html.format(tags)
    # html = html.replace("{tags}", tags)
    return HttpResponse(html)


def about(request):
    return render(request, 'about-b5.html', locals())

def about2(request):
    html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>about 2</title>
</head>
<body>
    <h2>some body by HttpResponse(html)</h2>
    <hr>
    
</body>
</html>
'''
    return HttpResponse(html)

def about3(request):
    html = '''
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>about</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <h1 class="display-4">Mobile Shop</h1>
        <p class="lead">Welcome to our small mobile phone shop.</p>
        <hr>
        <div class="row">
            <div class="col-sm-6">
                <div class="card">
                    <img src="https://picsum.photos/id/237/200/300" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">IPhone 12</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="#" class="btn btn-primary">Buy Now</a>
                    </div>
                </div>
            </div>
            <div class="col-sm-6">
                <div class="card">
                    <img src="https://picsum.photos/id/238/200/300" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Samsung S22</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="#" class="btn btn-primary">Buy Now</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <hr>
    
</body>
</html>
    
    '''
    return HttpResponse(html)

def disp_detail(request, id):
    try :
        product = Product.objects.get(id=id)
        print(product)
    except Product.DoesNotExist:
        # raise Http404("找不到商品")
        return HttpResponseNotFound('找不到商品')
    return render(request, 'disp.html', locals())

def about_author(request, author_id=0):
    html = f'Here is the about page for author {author_id}'
    print('path name url:', reverse('about_author'))
    print('path name url + args:', reverse('about_author', args=[author_id]))
    return JsonResponse({'message': html}, status=200)
    # return render(request, 'about_author.html', locals())
    # return HttpResponse(html)

def showpost_date(request, yr, mo, day):
    print(yr, mo, day)
    yr = 2001
    mo = 1
    day = 1
    
    html = '<a href="{}">Back</a>'.format(reverse('post_url', args=[yr, mo, day]))
    # return HttpResponse(html)
    return render(request, 'post_date.html', locals())

# 04 view & template練習習題
# 習題一
def student_list(request):
    students = [
        {'id': 1, 'name': '張小明', 'age': 20, 'class': 'A班'},
        {'id': 2, 'name': '李小華', 'age': 19, 'class': 'B班'},
        {'id': 3, 'name': '王小美', 'age': 21, 'class': 'A班'},
        {'id': 4, 'name': '陳小強', 'age': 20, 'class': 'C班'},
    ]
    # return render(request, 'student_list.html', {'students': students})
    return render(request, 'student_list.html', locals())

# 習題二
def student_grades(request):
    student_grades = [
        {'id': 1, 'name': '張小明', 'chinese': 85, 'math': 92, 'english': 78},
        {'id': 2, 'name': '李小華', 'chinese': 90, 'math': 76, 'english': 88},
        {'id': 3, 'name': '王小美', 'chinese': 72, 'english': 85, 'math': 90},
        {'id': 4, 'name': '陳小強', 'chinese': 88, 'math': 95, 'english': 82},
    ]
    
    # 計算平均分數 (在template中也可以使用custom filter)
    for student in student_grades:
        total = student['chinese'] + student['math'] + student['english']
        student['average'] = round(total / 3, 1)
    
    return render(request, 'student_grades.html', {'student_grades': student_grades})