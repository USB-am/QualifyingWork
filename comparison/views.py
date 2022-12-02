from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import ComparisonForm
from logics.analyzer import Analyzer, get_domain


class ComparisonView(FormView):
	''' Базовое представление страницы сравнения '''

	template_name = 'comparison/comparison.html'
	form_class = ComparisonForm
	success_url = 'index'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'Comparison of web pages'

		return context

	def get_success_url(self):
		url_1_input = self.request.POST.get('url_1')
		url_1 = get_domain(url_1_input)

		url_2_input = self.request.POST.get('url_2')
		url_2 = get_domain(url_2_input)

		if all((url_1, url_2)):
			return reverse_lazy('comparison_info', kwargs={
				'url_1': url_1,
				'url_2': url_2,
			})
		if all((url_1_input, url_2_input)):
			return reverse_lazy('comparison_info', kwargs={
				'url_1': url_1_input,
				'url_2': url_2_input,
			})

		return reverse_lazy('comparison')


class ComparisonInfoView(TemplateView):
	''' Базовое представление страницы информации о сравнении '''

	template_name = 'comparison/information.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = f'{context["url_1"]}/{context["url_2"]} - Comparison of web pages information'
		context['analyzer'] = Analyzer(context['url_1'])

		return context