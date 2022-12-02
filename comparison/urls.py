from django.urls import path

from .views import ComparisonView, ComparisonInfoView


urlpatterns = [
	path('', ComparisonView.as_view(), name='comparison'),
	path(
		'<str:url_1>/<str:url_2>',
		ComparisonInfoView.as_view(),
		name='comparison_info'
	),
]