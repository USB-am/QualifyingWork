from django.urls import path

from .views import ComparisonView, ComparisonInfoView


urlpatterns = [
	path('', ComparisonView.as_view(), name='comparison'),
	path(
		'<str:scheme_1>/<str:domain_1>/<str:scheme_2>/<str:domain_2>',
		ComparisonInfoView.as_view(),
		name='comparison_info'
	),
]