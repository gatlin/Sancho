from django.conf.urls import patterns, include, url
from rest_framework import routers
from api import views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'content-types', views.ContentTypeViewSet)
router.register(r'links', views.LinkViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sancho_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)
