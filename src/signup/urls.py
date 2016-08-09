"""
importing views and urls
"""

from django.conf.urls import url
from signup import views

urlpatterns = [

    url(r'^user/$', views.UserList.as_view()),
    url(r'^register/', views.CreateUserView.as_view(), name='user'),
    url(r'user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'user/update/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view()),
]
