from django.conf.urls import patterns
from django.contrib import admin
from mysite.views import *
from mysite.books import views, test1,backs,fronts
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^display$', display_meta),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    #(r'^search-form/$', views.search_form),
    (r'^search/$', views.search),
    (r'^contact/$', views.contact),
    (r'^test/$', test1.page),
    (r'^back/$', backs.regist),
    (r'^front/$', fronts.product),
    (r'^front/index1.html$',fronts.product),
    (r'^front/index2.html$',fronts.product),
    (r'^front/index3.html$',fronts.product),
    (r'^front/index4.html$',fronts.product),
    (r'^front/index5.html$',fronts.product),
    (r'^front/index6.html$',fronts.product),
    (r'^front/index7.html$',fronts.product),
    (r'^front/index8.html$',fronts.product),
    (r'^front/index9.html$',fronts.product),
    (r'^front/index10.html$',fronts.product),
)
