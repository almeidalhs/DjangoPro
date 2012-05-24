from django.conf.urls.defaults import *
from polls.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^DjangoPro/', include('DjangoPro.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^polls/$', 'DjangoPro.polls.views.index', name='show_Poll_index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'DjangoPro.polls.views.detail', name='show_Poll_detail'),
    (r'^polls/(?P<poll_id>\d+)/results/$', 'DjangoPro.polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'DjangoPro.polls.views.votes', name= 'vote_Poll'),

    (r'^instruct/$', 'DjangoPro.instructions.views.index'),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^hello_pdf/$', hello_pdf),
    (r'^display_meta/$', display_meta),
    (r'^date/$', current_datetime),
    (r'^hello_request/$', hello_request),

)
