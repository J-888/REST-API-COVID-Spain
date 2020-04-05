from django.conf.urls import url
from reports import views

urlpatterns = [
	url(r'^reports/$', views.ReportsApiView.as_view(), name='report-list'),
	url(r'^reports/(?P<pk>[0-9]+)/$', views.report_detail),
]