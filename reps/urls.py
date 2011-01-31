from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^',       include('django_reps.urls')),
    (r'^admin/', include(admin.site.urls)),
)

