from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, )
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True, )
    slug = models.SlugField(max_length=50, )
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-pub_date", ]

    def __str__(self):
        # pass
        return self.title

# use SNIPPET to create a new Post model with title, body, pub_date, slug fields
# add Meta class with verbose_name and verbose_name_plural    

# class Post1(models.Model):
#     title = models.CharField(max_length=255, )
#     body = models.TextField()
#     pub_date = models.DateTimeField(auto_now=False, auto_now_add=True, )
#     slug = models.SlugField(max_length=50, ) 

#     class Meta:
#         verbose_name = "Post1"
#         verbose_name_plural = "Post1s"

#     def __str__(self):
#         # pass
#         return self.title

# /*************   Windsurf Command   *************/
# use below prompt to Create your models here.
# create Post model with title, body, pub_date, slug fields
# add Meta class with verbose_name and verbose_name_plural
# /*************   Windsurf Command   *************/


# /*************   Windsurf Command   *************/
# class Post2(models.Model):
#     title = models.CharField(max_length=255, )
#     body = models.TextField()
#     pub_date = models.DateTimeField(auto_now=False, auto_now_add=True, )
#     slug = models.SlugField(max_length=50, ) 
#     class Meta:
#         verbose_name = "Post2"
#         verbose_name_plural = "Post2s"
#     def __str__(self):
#         # pass
#         return self.title
# /*******  d64bc91d-9404-4e09-a9dd-9ba0189c2317  *******/    

# /*************  Windsurf Command   *************/
class TangPoem(models.Model):
    title_author = models.CharField(max_length=200)
    content = models.TextField()

# Sample data insertion
poems = [
    TangPoem(content='床前明月光，疑是地上霜。舉頭望明月，低頭思故鄉。', title_author='李白 - 靜夜思'),
    TangPoem(content='國破山河在，城春草木深。感時花濺淚，恨別鳥驚心。', title_author='杜甫 - 春望'),
    TangPoem(content='白日依山盡，黃河入海流。欲窮千里目，更上一層樓。', title_author='王之涣 - 登鸛雀樓'),
    TangPoem(content='春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。', title_author='孟浩然 - 春曉'),
    TangPoem(content='空山不見人，但聞人語響。返景入深林，復照青苔上。', title_author='王維 - 鹿柴'),


# /*******  72d2c999-5c1b-4501-ab9d-0c7959a2981c  *******/    

    TangPoem(content='兩岸猿聲啼不住，light風回雪晚。青山相接處，行人跡難半。', title_author='李白 - 江上吟'),
    TangPoem(content='明月出天山，苔痕上架。疑是地上霜，舉頭望明月。', title_author='李白 - 蜀道難'),
    TangPoem(content='憶江南，憶江南，憶江南。春衫著起，憶江南。', title_author='白居易 -憶江南'),
    TangPoem(content='君不見黃河之水天上來，奔流到海不復回。君不見高堂明鏡悲白髮，早生華髮人生幾何。', title_author='李白 -將進酒'),
    TangPoem(content='床前明月光，疑是地上霜。舉頭望明月，低頭思故鄉。', title_author='李白 -靜夜思'),
]
