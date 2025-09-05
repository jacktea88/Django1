# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Avg, Count
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
import json
from datetime import datetime, timedelta

# 假設的模型 - 實際開發時需要對應的 models.py
from .models import (
    Product, Category, Review, NewsArticle, 
    TeamMember, Service, ContactMessage, Order
)
from .forms import ContactForm, ReviewForm


def home(request):
    """首頁視圖"""
    context = {
        'site_name': '我的網站',
        'news_list': [
            {
                'title': '全新產品線上線！',
                'date': timezone.now() - timedelta(days=1),
                'content': '我們很高興宣布推出全新的產品系列，為客戶提供更多選擇。這次的新品包含了多項創新功能...',
            },
            {
                'title': '春季特惠活動開始',
                'date': timezone.now() - timedelta(days=3),
                'content': '春季限時特惠活動正式開始！全館商品享有8折優惠，部分商品更有買一送一的超值優惠...',
            },
            {
                'title': '客戶服務時間調整通知',
                'date': timezone.now() - timedelta(days=7),
                'content': '為了提供更好的服務品質，我們的客服時間將調整為週一至週五 09:00-18:00...',
            },
            {
                'title': '網站維護完成公告',
                'date': timezone.now() - timedelta(days=10),
                'content': '感謝大家耐心等待，網站系統維護已完成。新版本加入了更多實用功能...',
            },
        ]
    }
    return render(request, 'home.html', context)


def about(request):
    """關於我們視圖"""
    team_members = [
        {
            'name': '張執行長',
            'position': '執行長兼創辦人',
            'photo': 'team/ceo.jpg',
            'description': '擁有15年軟體開發經驗，致力於創造優質的數位解決方案。'
        },
        {
            'name': '李技術長',
            'position': '技術長',
            'photo': 'team/cto.jpg',
            'description': '資深全端工程師，專精於系統架構設計和新技術導入。'
        },
        {
            'name': '王設計師',
            'position': '視覺設計總監',
            'photo': 'team/designer.jpg',
            'description': '創意設計專家，致力於打造令人驚豔的使用者體驗。'
        },
        {
            'name': '陳產品經理',
            'position': '產品經理',
            'photo': 'team/pm.jpg',
            'description': '產品策略專家，負責市場分析和產品規劃。'
        },
        {
            'name': '林客服經理',
            'position': '客戶服務經理',
            'photo': 'team/service.jpg',
            'description': '客戶關係管理專家，確保每位客戶都獲得最佳服務。'
        },
        {
            'name': '吳行銷經理',
            'position': '行銷經理',
            'photo': 'team/marketing.jpg',
            'description': '數位行銷專家，負責品牌推廣和市場開拓。'
        },
    ]
    
    context = {
        'team_members': team_members,
        'breadcrumb': [{'name': '關於我們', 'url': '#'}]
    }
    return render(request, 'about.html', context)


def services(request):
    """服務項目視圖"""
    # 獲取搜尋和篩選參數
    search = request.GET.get('search', '')
    category = request.GET.get('category', '')
    
    # 模擬服務資料
    all_services = [
        {
            'name': '響應式網頁設計',
            'category': 'web',
            'price': 50000,
            'description': '打造適合各種裝置的現代化網站，提供優質的使用者體驗。',
            'features': [
                '響應式設計，支援所有裝置',
                'SEO優化，提升搜尋排名',
                '快速載入，優化效能',
                '後台管理系統',
                '一年免費維護'
            ]
        },
        {
            'name': '電商網站開發',
            'category': 'web',
            'price': 120000,
            'description': '完整的電商解決方案，包含購物車、金流串接等功能。',
            'features': [
                '完整購物車系統',
                '多元金流串接',
                '庫存管理系統',
                '訂單管理後台',
                '會員管理功能'
            ]
        },
        {
            'name': 'iOS APP開發',
            'category': 'app',
            'price': 200000,
            'description': '原生iOS應用程式開發，提供最佳的使用者體驗。',
            'features': [
                '原生Swift開發',
                'App Store上架服務',
                '推播通知功能',
                '離線功能支援',
                '定期更新維護'
            ]
        },
        {
            'name': 'Android APP開發',
            'category': 'app',
            'price': 180000,
            'description': 'Android平台應用程式開發，支援各種Android設備。',
            'features': [
                '原生Kotlin開發',
                'Google Play上架',
                '多設備兼容',
                '雲端同步功能',
                '性能監控分析'
            ]
        },
        {
            'name': '跨平台APP開發',
            'category': 'app',
            'price': 250000,
            'description': '使用React Native或Flutter開發，一套程式支援雙平台。',
            'features': [
                '同時支援iOS/Android',
                '程式碼共用，降低成本',
                '原生效能表現',
                '快速開發部署',
                '統一維護更新'
            ]
        },
        {
            'name': 'ERP系統整合',
            'category': 'system',
            'price': 300000,
            'description': '企業資源規劃系統整合，提升營運效率。',
            'features': [
                '客製化系統設計',
                '現有系統整合',
                '資料移轉服務',
                '員工教育訓練',
                '長期技術支援'
            ]
        },
        {
            'name': 'CRM客戶管理系統',
            'category': 'system',
            'price': 180000,
            'description': '客戶關係管理系統，有效管理客戶資訊和銷售流程。',
            'features': [
                '客戶資料管理',
                '銷售流程追蹤',
                '行銷活動管理',
                '報表分析功能',
                '行動版支援'
            ]
        },
        {
            'name': '雲端服務架設',
            'category': 'system',
            'price': 100000,
            'description': '協助企業建置雲端基礎設施，提升系統可靠性。',
            'features': [
                'AWS/Azure部署',
                '自動擴展架構',
                '備份災難復原',
                '監控警報系統',
                '安全性防護'
            ]
        },
        {
            'name': 'UI/UX設計服務',
            'category': 'web',
            'price': 80000,
            'description': '專業的使用者介面和使用者體驗設計服務。',
            'features': [
                '使用者研究分析',
                '原型設計製作',
                '視覺設計規範',
                '互動效果設計',
                '可用性測試'
            ]
        },
    ]
    
    # 篩選服務
    services = all_services
    if search:
        services = [s for s in services if search.lower() in s['name'].lower() or search.lower() in s['description'].lower()]
    if category:
        services = [s for s in services if s['category'] == category]
    
    context = {
        'services': services,
        'search': search,
        'category': category,
    }
    return render(request, 'services.html', context)


def contact(request):
    """聯絡我們視圖"""
    if request.method == 'POST':
        # 處理聯絡表單提交
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        subject = request.POST.get('subject')
        message_content = request.POST.get('message')
        privacy = request.POST.get('privacy')
        
        if name and email and subject and message_content and privacy:
            # 儲存訊息到資料庫（需要 ContactMessage 模型）
            try:
                # contact_message = ContactMessage.objects.create(
                #     name=name,
                #     email=email,
                #     phone=phone,
                #     service=service,
                #     subject=subject,
                #     message=message_content,
                #     created_at=timezone.now()
                # )
                
                # 發送通知信件給管理員
                send_mail(
                    subject=f'網站聯絡表單：{subject}',
                    message=f'''
                    收到來自 {name} 的訊息：
                    
                    信箱：{email}
                    電話：{phone}
                    服務類型：{service}
                    
                    訊息內容：
                    {message_content}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                
                messages.success(request, '感謝您的來信！我們將會在24小時內回覆您。')
                return redirect('contact')
                
            except Exception as e:
                messages.error(request, '發送失敗，請稍後再試或直接撥打客服電話。')
        else:
            messages.error(request, '請填寫所有必填欄位並同意隱私權政策。')
    
    return render(request, 'contact.html')


class ProductListView(ListView):
    """產品列表視圖（使用類別視圖）"""
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True).select_related('category')
        
        # 搜尋功能
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | 
                Q(description__icontains=search) |
                Q(category__name__icontains=search)
            )
        
        # 分類篩選
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        
        # 價格篩選
        price_min = self.request.GET.get('price_min')
        price_max = self.request.GET.get('price_max')
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        
        # 評分篩選
        rating = self.request.GET.get('rating')
        if rating:
            queryset = queryset.filter(average_rating__gte=rating)
        
        # 特殊標籤篩選
        if self.request.GET.get('is_new'):
            queryset = queryset.filter(is_new=True)
        if self.request.GET.get('on_sale'):
            queryset = queryset.filter(on_sale=True)
        if self.request.GET.get('free_shipping'):
            queryset = queryset.filter(free_shipping=True)
        
        # 排序
        sort = self.request.GET.get('sort', '')
        if sort == 'name_asc':
            queryset = queryset.order_by('name')
        elif sort == 'name_desc':
            queryset = queryset.order_by('-name')
        elif sort == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort == 'rating_desc':
            queryset = queryset.order_by('-average_rating')
        elif sort == 'created_desc':
            queryset = queryset.order_by('-created_at')
        else:
            queryset = queryset.order_by('-created_at')  # 預設排序
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 添加模擬資料
        context['products'] = self.get_mock_products()
        return context
    
    def get_mock_products(self):
        """提供模擬產品資料"""
        import random
        
        products = []
        categories = ['electronics', 'fashion', 'home', 'sports']
        
        for i in range(1, 25):
            product = {
                'id': i,
                'name': f'精選商品 {i}',
                'category': random.choice(categories),
                'price': random.randint(500, 5000),
                'original_price': random.randint(600, 6000) if random.choice([True, False]) else None,
                'description': f'這是商品 {i} 的詳細描述，包含了產品的主要特色和功能說明。',
                'rating': random.randint(3, 5),
                'review_count': random.randint(10, 200),
                'is_new': random.choice([True, False]),
                'on_sale': random.choice([True, False]),
                'free_shipping': random.choice([True, False]),
                'stock': random.randint(0, 100),
                'discount': random.randint(10, 50) if random.choice([True, False]) else 0,
            }
            products.append(product)
        
        return products


def product_detail(request, product_id):
    """產品詳情視圖"""
    # 在實際應用中，這裡會從資料庫獲取產品
    # product = get_object_or_404(Product, id=product_id, is_active=True)
    
    # 模擬產品資料
    product = {
        'id': product_id,
        'name': f'精選商品 {product_id}',
        'category': 'electronics',
        'price': 1299,
        'original_price': 1599,
        'description': '這是一款精心設計的產品，結合了現代科技與優雅外觀。',
        'detailed_description': '''
        這款產品採用最新的技術，為用戶提供卓越的使用體驗。

        主要特色：
        • 採用高品質材料製造
        • 人性化設計，操作簡單
        • 節能環保，符合國際標準
        • 提供完整保固服務

        適用場景：
        無論是日常使用還是專業需求，這款產品都能滿足您的期望。
        ''',
        'rating': 4,
        'review_count': 156,
        'stock': 25,
        'is_new': True,
        'on_sale': True,
        'free_shipping': True,
        'has_variants': True,
        'variants': [
            {'id': 1, 'name': '標準版'},
            {'id': 2, 'name': '專業版'},
            {'id': 3, 'name': '旗艦版'},
        ],
        'features': [
            '高品質材料製造',
            '人性化設計界面',
            '節能環保認證',
            '兩年品質保證',
            '24小時客服支援'
        ],
        'specifications': [
            {'name': '品牌', 'value': '我的品牌'},
            {'name': '型號', 'value': f'Model-{product_id}'},
            {'name': '尺寸', 'value': '30 x 20 x 10 cm'},
            {'name': '重量', 'value': '1.2 kg'},
            {'name': '材質', 'value': '優質塑料+金屬'},
            {'name': '保固', 'value': '2年'},
            {'name': '產地', 'value': '台灣'},
        ],
        'reviews': [
            {
                'id': 1,
                'user': {'username': 'user1', 'get_full_name': lambda: '張小明'},
                'rating': 5,
                'comment': '產品品質很好，使用起來很順手，推薦給大家！',
                'created_at': timezone.now() - timedelta(days=5),
                'helpful_count': 12,
                'images': []
            },
            {
                'id': 2,
                'user': {'username': 'user2', 'get_full_name': lambda: '李小華'},
                'rating': 4,
                'comment': '整體來說不錯，CP值很高，但包裝可以再改進。',
                'created_at': timezone.now() - timedelta(days=15),
                'helpful_count': 8,
                'images': []
            },
            {
                'id': 3,
                'user': {'username': 'user3', 'get_full_name': lambda: '王大明'},
                'rating': 5,
                'comment': '超出期待！功能豐富，設計精美，值得購買。',
                'created_at': timezone.now() - timedelta(days=30),
                'helpful_count': 15,
                'images': []
            }
        ],
        'rating_breakdown': [
            {'stars': 5, 'count': 89, 'percentage': 57},
            {'stars': 4, 'count': 45, 'percentage': 29},
            {'stars': 3, 'count': 15, 'percentage': 10},
            {'stars': 2, 'count': 5, 'percentage': 3},
            {'stars': 1, 'count': 2, 'percentage': 1},
        ],
        'faqs': [
            {
                'question': '這個產品適合初學者使用嗎？',
                'answer': '是的，我們的產品設計時特別考慮了易用性，提供詳細的使用說明和教學影片，非常適合初學者使用。'
            },
            {
                'question': '保固期間是多久？',
                'answer': '我們提供兩年的品質保證，在保固期間內如有任何品質問題，我們將提供免費維修或更換服務。'
            },
            {
                'question': '是否提供技術支援？',
                'answer': '是的，我們有專業的技術支援團隊，提供24小時線上客服，您可以隨時聯繫我們尋求協助。'
            },
            {
                'question': '可以退貨嗎？',
                'answer': '購買後7天內，如商品未使用且包裝完整，可申請退貨。退貨運費由客戶負擔。'
            }
        ]
    }
    
    # 相關產品（模擬）
    related_products = [
        {
            'id': i,
            'name': f'相關商品 {i}',
            'price': 999 + i * 100,
            'rating': 4 + (i % 2),
        }
        for i in range(1, 5)
    ]
    
    context = {
        'product': product,
        'related_products': related_products,
        'breadcrumb': [
            {'name': '產品列表', 'url': reverse('product_list')},
            {'name': product['name'], 'url': '#'}
        ]
    }
    
    return render(request, 'product_detail.html', context)


@login_required
@require_POST
def add_review(request, product_id):
    """添加商品評論"""
    # product = get_object_or_404(Product, id=product_id)
    
    rating = request.POST.get('rating')
    comment = request.POST.get('comment')
    
    if rating and comment:
        # 在實際應用中，這裡會創建 Review 物件
        # Review.objects.create(
        #     product=product,
        #     user=request.user,
        #     rating=int(rating),
        #     comment=comment
        # )
        
        messages.success(request, '感謝您的評論！')
    else:
        messages.error(request, '請填寫評分和評論內容。')
    
    return redirect('product_detail', product_id=product_id)


@require_POST
def add_to_cart(request):
    """加入購物車（AJAX）"""
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        variant_id = request.POST.get('variant_id')
        
        # 處理購物車邏輯
        cart = request.session.get('cart', {})
        
        key = f"{product_id}_{variant_id}" if variant_id else str(product_id)
        
        if key in cart:
            cart[key]['quantity'] += quantity
        else:
            cart[key] = {
                'product_id': product_id,
                'variant_id': variant_id,
                'quantity': quantity
            }
        
        request.session['cart'] = cart
        
        return JsonResponse({
            'success': True,
            'message': '商品已加入購物車',
            'cart_count': sum(item['quantity'] for item in cart.values())
        })
    
    return JsonResponse({'success': False, 'message': '無效的請求'})


def custom_login(request):
    """自訂登入視圖"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, '帳號或密碼錯誤')
    
    return render(request, 'registration/login.html')


def custom_register(request):
    """自訂註冊視圖"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '註冊成功！請登入您的帳號。')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def custom_logout(request):
    """自訂登出視圖"""
    logout(request)
    messages.success(request, '您已成功登出')
    return redirect('home')


# urls.py
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # 管理後台
    path('admin/', admin.site.urls),
    
    # 首頁
    path('', views.home, name='home'),
    
    # 靜態頁面
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    
    # 產品相關
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/<int:product_id>/review/', views.add_review, name='add_review'),
    
    # 購物車功能
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    
    # 使用者認證
    path('login/', views.custom_login, name='login'),
    path('register/', views.custom_register, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    
    # 可以加入更多URL模式
    # path('cart/', views.cart_view, name='cart'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('orders/', views.order_history, name='orders'),
    # path('profile/', views.profile, name='profile'),
]

# 在開發環境中提供媒體文件
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# 額外的 URL 設定檔案，可以拆分成多個 app
# apps/products/urls.py
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('<int:product_id>/', views.product_detail, name='detail'),
    path('<int:product_id>/review/', views.add_review, name='add_review'),
    path('category/<slug:category_slug>/', views.ProductListView.as_view(), name='by_category'),
    path('search/', views.ProductListView.as_view(), name='search'),
]

# apps/accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('register/', views.custom_register, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]

# 主要的 urls.py（當使用多個 app 時）
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('about/', main_views.about, name='about'),
    path('services/', main_views.services, name='services'),
    path('contact/', main_views.contact, name='contact'),
    
    # 包含各個 app 的 URL
    path('products/', include('apps.products.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('cart/', include('apps.cart.urls')),
    path('orders/', include('apps.orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# 自訂 Template Filter（需要在 templatetags/custom_filters.py）
from django import template
from django.utils.safestring import mark_safe
from django.utils.http import urlencode
import re

register = template.Library()

@register.filter
def get_category_display(value):
    """獲取分類顯示名稱"""
    category_choices = {
        'electronics': '3C電子',
        'fashion': '時尚服飾', 
        'home': '居家生活',
        'sports': '運動休閒'
    }
    return category_choices.get(value, value)

@register.filter
def multiply(value, arg):
    """數字相乘"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0


# models.py（範例模型定義）
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    """商品分類"""
    name = models.CharField('分類名稱', max_length=100)
    slug = models.SlugField('網址代碼', unique=True)
    description = models.TextField('分類描述', blank=True)
    image = models.ImageField('分類圖片', upload_to='categories/', blank=True)
    is_active = models.BooleanField('是否啟用', default=True)
    sort_order = models.PositiveIntegerField('排序', default=0)
    created_at = models.DateTimeField('建立時間', auto_now_add=True)
    updated_at = models.DateTimeField('更新時間', auto_now=True)
    
    class Meta:
        verbose_name = '商品分類'
        verbose_name_plural = '商品分類'
        ordering = ['sort_order', 'name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_list') + f'?category={self.slug}'


class Product(models.Model):
    """商品模型"""
    name = models.CharField('商品名稱', max_length=200)
    slug = models.SlugField('網址代碼', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分類')
    description = models.TextField('簡短描述')
    detailed_description = models.TextField('詳細描述', blank=True)
    
    # 價格相關
    price = models.DecimalField('售價', max_digits=10, decimal_places=2)
    original_price = models.DecimalField('原價', max_digits=10, decimal_places=2, null=True, blank=True)
    cost_price = models.DecimalField('成本價', max_digits=10, decimal_places=2, null=True, blank=True)
    
    # 庫存管理
    stock = models.PositiveIntegerField('庫存數量', default=0)
    min_stock = models.PositiveIntegerField('最低庫存', default=5)
    
    # 商品圖片
    main_image = models.ImageField('主要圖片', upload_to='products/')
    
    # 商品狀態
    is_active = models.BooleanField('是否上架', default=True)
    is_new = models.BooleanField('新品', default=False)
    on_sale = models.BooleanField('特價中', default=False)
    free_shipping = models.BooleanField('免運費', default=False)
    
    # 評分（非正規化，用於效能）
    average_rating = models.FloatField('平均評分', default=0)
    review_count = models.PositiveIntegerField('評論數量', default=0)
    
    # SEO相關
    meta_title = models.CharField('頁面標題', max_length=200, blank=True)
    meta_description = models.TextField('頁面描述', blank=True)
    
    # 時間戳記
    created_at = models.DateTimeField('建立時間', auto_now_add=True)
    updated_at = models.DateTimeField('更新時間', auto_now=True)
    
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['category', 'is_active']),
            models.Index(fields=['price']),
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_id': self.pk})
    
    @property
    def is_in_stock(self):
        return self.stock > 0
    
    @property
    def is_low_stock(self):
        return self.stock <= self.min_stock
    
    @property
    def discount_percentage(self):
        if self.original_price and self.original_price > self.price:
            return int((1 - self.price / self.original_price) * 100)
        return 0
    
    @property
    def savings(self):
        if self.original_price and self.original_price > self.price:
            return self.original_price - self.price
        return 0
    
    def update_rating(self):
        """更新商品評分"""
        reviews = self.reviews.filter(is_approved=True)
        if reviews.exists():
            self.average_rating = reviews.aggregate(
                avg_rating=models.Avg('rating')
            )['avg_rating']
            self.review_count = reviews.count()
        else:
            self.average_rating = 0
            self.review_count = 0
        self.save(update_fields=['average_rating', 'review_count'])


class ProductImage(models.Model):
    """商品圖片"""
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('圖片', upload_to='products/')
    alt_text = models.CharField('替代文字', max_length=200, blank=True)
    sort_order = models.PositiveIntegerField('排序', default=0)
    is_active = models.BooleanField('是否顯示', default=True)
    
    class Meta:
        verbose_name = '商品圖片'
        verbose_name_plural = '商品圖片'
        ordering = ['sort_order']
    
    def __str__(self):
        return f'{self.product.name} - 圖片 {self.sort_order}'


class ProductVariant(models.Model):
    """商品規格"""
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    name = models.CharField('規格名稱', max_length=100)
    price_adjustment = models.DecimalField('價格調整', max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField('庫存', default=0)
    sku = models.CharField('SKU', max_length=100, unique=True)
    is_active = models.BooleanField('是否啟用', default=True)
    sort_order = models.PositiveIntegerField('排序', default=0)
    
    class Meta:
        verbose_name = '商品規格'
        verbose_name_plural = '商品規格'
        ordering = ['sort_order']
        unique_together = [['product', 'name']]
    
    def __str__(self):
        return f'{self.product.name} - {self.name}'
    
    @property
    def final_price(self):
        return self.product.price + self.price_adjustment


class Review(models.Model):
    """商品評論"""
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        '評分', 
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    title = models.CharField('標題', max_length=200, blank=True)
    comment = models.TextField('評論內容')
    
    # 狀態管理
    is_approved = models.BooleanField('已審核', default=True)
    is_verified_purchase = models.BooleanField('已驗證購買', default=False)
    
    # 互動數據
    helpful_count = models.PositiveIntegerField('有用數', default=0)
    
    # 時間戳記
    created_at = models.DateTimeField('建立時間', auto_now_add=True)
    updated_at = models.DateTimeField('更新時間', auto_now=True)
    
    class Meta:
        verbose_name = '商品評論'
        verbose_name_plural = '商品評論'
        ordering = ['-created_at']
        unique_together = [['product', 'user']]  # 一個使用者只能評論一次
    
    def __str__(self):
        return f'{self.user.username} - {self.product.name} ({self.rating}星)'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # 更新商品評分
        self.product.update_rating()


class ReviewImage(models.Model):
    """評論圖片"""
    review = models.ForeignKey(Review, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('圖片', upload_to='reviews/')
    
    class Meta:
        verbose_name = '評論圖片'
        verbose_name_plural = '評論圖片'


class NewsArticle(models.Model):
    """新聞文章"""
    title = models.CharField('標題', max_length=200)
    slug = models.SlugField('網址代碼', unique=True)
    content = models.TextField('內容')
    excerpt = models.TextField('摘要', blank=True)
    featured_image = models.ImageField('特色圖片', upload_to='news/', blank=True)
    
    is_published = models.BooleanField('已發布', default=False)
    is_featured = models.BooleanField('精選文章', default=False)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    views = models.PositiveIntegerField('觀看次數', default=0)
    
    published_at = models.DateTimeField('發布時間', null=True, blank=True)
    created_at = models.DateTimeField('建立時間', auto_now_add=True)
    updated_at = models.DateTimeField('更新時間', auto_now=True)
    
    class Meta:
        verbose_name = '新聞文章'
        verbose_name_plural = '新聞文章'
        ordering = ['-published_at', '-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)


class TeamMember(models.Model):
    """團隊成員"""
    name = models.CharField('姓名', max_length=100)
    position = models.CharField('職位', max_length=100)
    bio = models.TextField('個人簡介', blank=True)
    photo = models.ImageField('照片', upload_to='team/')
    email = models.EmailField('電子信箱', blank=True)
    linkedin = models.URLField('LinkedIn', blank=True)
    
    is_active = models.BooleanField('是否顯示', default=True)
    sort_order = models.PositiveIntegerField('排序', default=0)
    
    created_at = models.DateTimeField('加入時間', auto_now_add=True)
    
    class Meta:
        verbose_name = '團隊成員'
        verbose_name_plural = '團隊成員'
        ordering = ['sort_order', 'name']
    
    def __str__(self):
        return f'{self.name} - {self.position}'


class Service(models.Model):
    """服務項目"""
    CATEGORY_CHOICES = [
        ('web', '網頁設計'),
        ('app', 'APP開發'),
        ('system', '系統整合'),
        ('design', '設計服務'),
        ('consulting', '諮詢服務'),
    ]
    
    name = models.CharField('服務名稱', max_length=200)
    slug = models.SlugField('網址代碼', unique=True)
    category = models.CharField('分類', max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField('簡短描述')
    detailed_description = models.TextField('詳細描述', blank=True)
    
    price_from = models.DecimalField('起始價格', max_digits=10, decimal_places=2)
    features = models.JSONField('服務特色', default=list)
    
    icon = models.CharField('圖示類別', max_length=50, blank=True)
    image = models.ImageField('服務圖片', upload_to='services/', blank=True)
    
    is_active = models.BooleanField('是否啟用', default=True)
    is_featured = models.BooleanField('精選服務', default=False)
    sort_order = models.PositiveIntegerField('排序', default=0)
    
    created_at = models.DateTimeField('建立時間', auto_now_add=True)
    updated_at = models.DateTimeField('更新時間', auto_now=True)
    
    class Meta:
        verbose_name = '服務項目'
        verbose_name_plural = '服務項目'
        ordering = ['sort_order', 'name']
    
    def __str__(self):
        return self.name
    
    def get_category_display(self):
        return dict(self.CATEGORY_CHOICES).get(self.category, self.category)


class ContactMessage(models.Model):
    """聯絡訊息"""
    name = models.CharField('姓名', max_length=100)
    email = models.EmailField('電子信箱')
    phone = models.CharField('電話', max_length=20, blank=True)
    subject = models.CharField('主旨', max_length=200)
    message = models.TextField('訊息內容')
    service = models.CharField('服務類型', max_length=50, blank=True)
    
    is_read = models.BooleanField('已讀取', default=False)
    is_replied = models.BooleanField('已回覆', default=False)
    
    created_at = models.DateTimeField('收到時間', auto_now_add=True)
    replied_at = models.DateTimeField('回覆時間', null=True, blank=True)
    
    class Meta:
        verbose_name = '聯絡訊息'
        verbose_name_plural = '聯絡訊息'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.name} - {self.subject}'


# forms.py（表單定義）
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review, ContactMessage

class ContactForm(forms.ModelForm):
    """聯絡表單"""
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message', 'service']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '請輸入您的姓名'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '請輸入電子信箱'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '請輸入聯絡電話'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '請輸入主旨'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': '請輸入詳細訊息內容'
            }),
            'service': forms.Select(attrs={
                'class': 'form-select'
            }, choices=[
                ('', '請選擇服務類型'),
                ('web', '網頁設計'),
                ('app', 'APP開發'),
                ('system', '系統整合'),
                ('other', '其他')
            ])
        }


class ReviewForm(forms.ModelForm):
    """評論表單"""
    class Meta:
        model = Review
        fields = ['rating', 'title', 'comment']
        widgets = {
            'rating': forms.Select(choices=[
                ('', '請選擇評分'),
                (5, '5星 - 非常滿意'),
                (4, '4星 - 滿意'),
                (3, '3星 - 普通'),
                (2, '2星 - 不滿意'),
                (1, '1星 - 非常不滿意'),
            ], attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '評論標題（可選）'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': '請分享您的使用心得'
            })
        }


class CustomUserCreationForm(UserCreationForm):
    """自訂註冊表單"""
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


# admin.py（管理後台配置）
from django.contrib import admin
from .models import (
    Category, Product, ProductImage, ProductVariant,
    Review, ReviewImage, NewsArticle, TeamMember,
    Service, ContactMessage
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'sort_order', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['sort_order', 'name']

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'is_new', 'on_sale', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductVariantInline]
    ordering = ['-created_at']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_approved', 'created_at']
    search_fields = ['comment', 'user__username', 'product__name']
    ordering = ['-created_at']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'is_replied', 'service', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
def highlight(text, search):
    """高亮搜尋關鍵字"""
    if not search:
        return text
    
    highlighted = re.sub(
        f'({re.escape(search)})', 
        r'<span class="search-highlight">\1</span>', 
        str(text), 
        flags=re.IGNORECASE
    )
    return mark_safe(highlighted)

@register.simple_tag(takes_context=True)
def url_replace(context, field, value):
    """替換URL參數"""
    request = context['request']
    dict_ = request.GET.copy()
    dict_[field] = value
    return '&'.join([f'{k}={v}' for k, v in dict_.items()])

@register.filter