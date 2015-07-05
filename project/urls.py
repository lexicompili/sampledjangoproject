from django.conf import settings # add this
from django.conf.urls.static import static # add this
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^(?P<category_slug>[-\w]+)/$', views.category), # add this
    url(r'^(?P<category_slug>[-\w]+)/(?P<recipe_id>\d+)/([-\w]+)/$', views.recipe), # add this
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
