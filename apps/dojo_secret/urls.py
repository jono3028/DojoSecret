# APP: dojo_secrets
from django.conf.urls import url, include
from . import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'home'),
    url(r'^post$', views.postSecret, name = 'post'),
    url(r'^popular$', views.mostPopular, name = 'popular'),
    url(r'^post/(?P<post_id>\d+)$', views.deleteSecret, name = 'delete'),
    url(r'^like/(?P<post_id>\d+)$', views.likeSecret, name = 'like'),

]
