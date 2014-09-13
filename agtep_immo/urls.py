from django.conf.urls import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agtep_immo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    #url(r'^presentation/', include('presentation.urls')),

    url(r'^$', 'presentation.views.accueil', name="accueil"),
    url(r'^services/$', 'presentation.views.services', name="services"),
    url(r'^offres/$', 'presentation.views.offres', name="offres"),
    url(r'^contacts/$', 'presentation.views.contact', name="contact"),

)

urlpatterns += staticfiles_urlpatterns()