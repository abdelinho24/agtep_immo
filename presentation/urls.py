from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('presentation.views',
    # Examples:
    # url(r'^$', 'crepes_bretonnes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accueil/$', 'accueil'),
    url(r'^services/$', 'services'),
    url(r'^offres/$', 'offres'),
    url(r'^contacts/$', 'contact'),
   
)