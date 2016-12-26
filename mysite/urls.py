from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views
from log.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('personal.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'', include('log.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    #url(r'^logout/$', views.logout, {'next_page': '/LoginRequest'}),
    
]
