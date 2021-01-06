"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from django.conf import settings
from django.conf.urls.static import static

from shop.views import info, contacts, feedback
urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', info),
    path('contacts/', contacts),
    path('feedback/', feedback),
    # url(r'^info/', include(('shop.urls', 'info'), namespace='info')),
    url(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
    url(r'^orders/', include(('orders.urls', 'orders'), namespace='orders')),
    url(r'^', include(('shop.urls', 'shop'), namespace='shop')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
