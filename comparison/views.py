from urllib.parse import urlparse

from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import ComparisonForm
from logics import Site


def get_domain(url: str) -> str:
	parsed_url = urlparse(url)
	scheme = parsed_url.scheme
	domain = parsed_url.netloc

	return (scheme, domain)


def input_to_domain(scheme: str, domain: str) -> str:
	return f'{scheme}://{domain}'


class ComparisonSitesView(FormView):
	''' Базовое представление страницы сравнения сайтов '''

	template_name = 'comparison/comparison.html'
	form_class = ComparisonForm
	success_url = 'index'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'Comparison of web sites'

		return context

	def get_success_url(self):
		url_1 = self.request.POST.get('url_1')
		url_2 = self.request.POST.get('url_2')
		scheme_1, domain_1 = get_domain(url_1)
		scheme_2, domain_2 = get_domain(url_2)

		return reverse_lazy(
			viewname='comparison_sites_info',
			kwargs={
				'scheme_1': scheme_1, 'domain_1': domain_1,
				'scheme_2': scheme_2, 'domain_2': domain_2,
			}
		)


class ComparisonPagesView(FormView):
	''' Базовое представление страницы сравнения веб-страниц '''

	template_name = 'comparison/comparison.html'
	form_class = ComparisonForm
	success_url = 'index'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'Comparison of web pages'

		return context

	def get_success_url(self):
		url_1 = self.request.POST.get('url_1')
		url_2 = self.request.POST.get('url_2')
		scheme_1, domain_1 = get_domain(url_1)
		scheme_2, domain_2 = get_domain(url_2)

		return reverse_lazy(
			viewname='comparison_pages_info',
			kwargs={
				'scheme_1': scheme_1, 'domain_1': domain_1,
				'scheme_2': scheme_2, 'domain_2': domain_2,
			}
		)


class ComparisonSitesInfoView(TemplateView):
	''' Базовое представление страницы информации о сравнении сайтов '''

	template_name = 'comparison/information.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = f'{context["domain_1"]}/{context["domain_2"]}' +\
			' - Comparison of web sites information'
		context['site_1'] = Site(
			input_to_domain(context['scheme_1'], context['domain_1'])
		)
		context['site_2'] = Site(
			input_to_domain(context['scheme_2'], context['domain_2'])
		)

		return context


class ComparisonPagesInfoView(TemplateView):
	''' Базовое представление страницы информации о сравнении веб-страниц '''

	template_name = 'comparison/information.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = f'{context["domain_1"]}/{context["domain_2"]}' +\
			' - Comparison of web pages information'
		context['site_1'] = Site(
			input_to_domain(context['scheme_1'], context['domain_1'])
		)
		context['site_2'] = Site(
			input_to_domain(context['scheme_2'], context['domain_2'])
		)

		return context