from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from boards.views import fix_boss
from . import views



urlpatterns = [
    path('fix-boss/', fix_boss),
    path('', views.store, name='store'),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('update_item/',views.updateItem, name='update_item'),
    path('process_order/',views.processOrder, name='process_order'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)