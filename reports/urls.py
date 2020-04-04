from django.conf.urls import url
from reports import views
# from reports.views import ReportsListView

urlpatterns = [
	url(r'^reports/$', views.report_list),
	url(r'^reports/(?P<pk>[0-9]+)/$', views.report_detail),
	# url(r'^reports/$', ReportsListView.as_view()),
]