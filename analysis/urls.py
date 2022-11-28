from django.urls import path

from .views import AnalysisView, AnalysisInfoView


urlpatterns = [
	path('', AnalysisView.as_view(), name='analysis'),
	path('<str:url>/', AnalysisInfoView.as_view(), name='analysis_info')
]