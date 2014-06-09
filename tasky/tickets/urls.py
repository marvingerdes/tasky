from django.conf.urls import patterns, include, url

urlpatterns = patterns("tasky.tickets.views",
#    url(r"^$", "tickets_list"),
    url(r"^(?P<id>\d+)$", "tickets_detail"),
)
