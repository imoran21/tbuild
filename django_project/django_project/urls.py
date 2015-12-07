from django.conf.urls import patterns, include, url

from tb import urls as tb_urls
from tb import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tb/', include(tb_urls)),
    url(r'^$', views.home, name='home'),
)
