from django.conf.urls import url
from news import views


urlpatterns = [
    url(r'^articles/$', 
        views.ArticleList.as_view(),
        name=views.ArticleList.name),
    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
    url(r'^articles/(?P<pk>[0-9]+)/$', 
        views.ArticleDetail.as_view(),
        name=views.ArticleDetail.name),
    url(r'^users/$',
        views.UserList.as_view(),
        name=views.UserList.name),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name=views.UserDetail.name),
]
