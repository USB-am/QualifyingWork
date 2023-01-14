from django.urls import path

from .views import ComparisonSitesView, ComparisonPagesView, \
	ComparisonSitesInfoView, ComparisonPagesInfoView


urlpatterns = [
	path('sites/', ComparisonSitesView.as_view(), name='sites_comparison'),
	path(
		'sites/<str:scheme_1>/<str:domain_1>/<str:scheme_2>/<str:domain_2>',
		ComparisonSitesInfoView.as_view(),
		name='comparison_sites_info'
	),
	path('pages/', ComparisonPagesView.as_view(), name='pages_comparison'),
	path(
		'pages/<str:scheme_1>/<str:domain_1>/<str:scheme_2>/<str:domain_2>',
		ComparisonPagesInfoView.as_view(),
		name='comparison_pages_info'
	),
]