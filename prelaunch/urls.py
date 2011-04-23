from django.conf.urls.defaults import *
import views, forms

urlpatterns = patterns('',
    (r'^$', forms.prelaunch),
    (r'^r/(?P<referrer>.*)/$', views.referrer),
)
