from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^info$', views.info, name='info'),

    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]