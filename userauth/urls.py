from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('soundsynth.userauth.views',
    url(r'^register/$','register',name="auth_register"),
    url(r'^login/$','login',name="auth_login"),
    url(r'^logout/$','logout',name="auth_logout"),
)

