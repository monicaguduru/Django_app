from django.conf.urls import url
from . import views

app_name='sensors'

urlpatterns = [
    # /sensors/
    url(r'^$', views.aaa , name='index'),
    url(r'^display/$', views.new_disp, name="new_disp"),
    url(r'^display/index.html/$', views.index, name="new_disp"),
    url(r'^display/second.html/$', views.second, name="new_disp"),
    url(r'^display/teri.html/$', views.teri, name="new_disp"),
    url(r'^display/maps.html/$', views.maps, name="new_disp"),
url(r'^display/(?P<ps>[0-9]+.[0-9]+)/(?P<ss>[0-9]+.[0-9]+)/(?P<dw>[0-9]+.[0-9]+)/(?P<spw>[0-9]+.[0-9]+)/(?P<tpw>[0-9]+.?[0-9]*)/',views.Display,name="Display"),
]
