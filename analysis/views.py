from urllib.parse import urlparse

from requests.exceptions import ConnectionError

from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import AnalysisForm
from logics import Site, Page


def get_domain(url: str) -> str:
	if url[-1] == '/':
		url = url[:-1]

	parsed_url = urlparse(url)
	scheme = parsed_url.scheme
	domain = parsed_url.netloc
	path = '+'.join(parsed_url.path.split('/')[1:])

	return (scheme, domain, path)


class AnalysisSiteView(FormView):
	''' Базовое представление страцы с анализом '''

	template_name = 'analysis/analysis.html'
	form_class = AnalysisForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'Analyze a web site - USBAM'

		return context

	def get_success_url(self):
		url_input = self.request.POST.get('url')
		scheme, url, _ = get_domain(url_input)

		return reverse_lazy(
			viewname='analysis_site_info',
			kwargs={'scheme': scheme, 'url': url}
		)


class AnalysisPageView(FormView):
	''' Базовое представление страцы с анализом '''

	template_name = 'analysis/analysis.html'
	form_class = AnalysisForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'Analyze a web page - USBAM'

		return context

	def get_success_url(self):
		url_input = self.request.POST.get('url')
		scheme, url, path = get_domain(url_input)
		return reverse_lazy(
			viewname='analysis_page_info',
			kwargs={'scheme': scheme, 'url': f'{url}+{path}'}
		)


def input_to_domain(scheme: str, netloc: str) -> str:
	return f'{scheme}://{netloc}'


class AnalysisSiteInfoView(TemplateView):
	''' Базовое представление страницы с информацией сайта '''

	template_name = 'analysis/information.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'Analysis site Info'
		context['data'] = Site(
			input_to_domain(context['scheme'], context['url'])
		)

		return context


class AnalysisPageInfoView(TemplateView):
	''' Базовое представление страницы с информацией страницы '''

	template_name = 'analysis/information.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'Analysis page Info'
		page_url = input_to_domain(context['scheme'], context['url'])\
			.replace('+', '/')

		context['data'] = Page(page_url)

		return context