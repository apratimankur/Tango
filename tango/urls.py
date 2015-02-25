from django.conf.urls import patterns, include, url
from django.contrib import admin
import app1.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', app1.views.index, name='homepage'),
    url(r'^ankur/$', app1.views.ankur, name='ankur'),
    url(r'^register/$', app1.views.register, name='register'),
)