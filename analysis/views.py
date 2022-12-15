from requests.exceptions import ConnectionError

from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import AnalysisForm
from logics.analyzer import Analyzer, get_domain


class AnalysisView(FormView):
	''' Базовое представление страцы с анализом '''

	template_name = 'analysis/analysis.html'
	form_class = AnalysisForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'Analyze a web page - USBAM'

		return context

	def get_success_url(self):
		url_input = self.request.POST.get('url')
		url = get_domain(url_input)

		if url:
			return reverse_lazy('analysis_info', kwargs={'url': url})
		if url_input:
			return reverse_lazy('analysis_info', kwargs={'url': url_input})
		return reverse_lazy('index')


class AnalysisInfoView(TemplateView):
	''' Базовое представление страницы с информацией '''

	template_name = 'analysis/information.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'Analysis Info page'
		try:
			context['analyzer'] = Analyzer(context['url'])
		except ConnectionError:
			context['error'] = 'Url is invalid!'

		return context