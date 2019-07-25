from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/', views.get_search, name='get_search'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^update/profile/(\d+)$', views.update_profile, name='update-profile'),
    url(r'^post/image/(\d+)$', views.post_image, name='post_image'),
    url(r'^post/comment/(\d+)$', views.post_comment, name='post_comment'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
