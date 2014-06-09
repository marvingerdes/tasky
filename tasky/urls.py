from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tasky.views.home', name='home'),
    url(r"^tickets/", include("tasky.tickets.urls")),

    url(r'^admin/', include(admin.site.urls)),
)
