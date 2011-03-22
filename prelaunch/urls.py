from django.conf.urls.defaults import *
from django.conf import settings
import views, forms

urlpatterns = patterns('',
    (r'^$', forms.prelaunch),
    (r'^r/(?P<referrer>.*)/$', views.referrer),
)
