"""
importing views and urls
"""

from django.conf.urls import url
from signup import views
from django.conf.urls.static import static
from django.conf import settings

from django.conf import settings
urlpatterns = [

    url(r'^user/$', views.UserList.as_view()),
    url(r'^register/', views.CreateUserView.as_view(), name='user'),
    url(r'user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'user/update/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view()),
    url(r'user/upload/$', views.PhotoList.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
