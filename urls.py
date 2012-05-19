from django.conf.urls.defaults import patterns, include, url
import os
import ingeconomica.views
from django.conf import settings
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ingeconomica.views.home', name='home'),
    # url(r'^ingeconomica/', include('ingeconomica.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio/',ingeconomica.views.incio),
    #formato de url
    #/ingreso/depreciacion/ibanco/inversion/financiamiento/n/
    url(r'^P01/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$',ingeconomica.views.plan01),
    url(r'^P02/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$',ingeconomica.views.plan02),
    url(r'^P03/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$',ingeconomica.views.plan03),
    url(r'^P04/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$',ingeconomica.views.plan04),
    #url(r'^simple.png/', 'ingeconomica.views.simple'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

)
