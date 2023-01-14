from django.urls import path

from .views import AnalysisSiteView, AnalysisPageView, AnalysisSiteInfoView, AnalysisPageInfoView


urlpatterns = [
	path('site/', AnalysisSiteView.as_view(), name='site_analysis'),
	path('site/<str:scheme>/<str:url>/', AnalysisSiteInfoView.as_view(), name='analysis_site_info'),
	path('page/', AnalysisPageView.as_view(), name='page_analysis'),
	path('page/<str:scheme>/<str:url>/', AnalysisPageInfoView.as_view(), name='analysis_page_info'),
]