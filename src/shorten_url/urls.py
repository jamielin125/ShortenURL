
from django.conf.urls import url
from django.contrib import admin

from shortener.views import Homeview, URLRedirectview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Homeview),
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectview, name='scode'), 

]
