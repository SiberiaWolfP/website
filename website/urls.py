from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^login/$', views.login),
	url(r'^user/$', views.user),
	url(r'^login/search_result/$', views.user),
	url(r'^logout/$', views.logout_view),
	url(r'^main/$', views.main),
	#url(r'^edit/$', views.edit)
	
	]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)