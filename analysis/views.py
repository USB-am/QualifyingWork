from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import AnalysisForm
from logics.analyzer import Analyzer


class AnalysisView(FormView):
	''' Базовое представление страцы с анализом '''

	template_name = 'analysis/analysis.html'
	form_class = AnalysisForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'AnalysisView'

		return context

	def get_success_url(self):
		next_url = self.request.POST.get('url')

		if next_url:
			return reverse_lazy('analysis_info', kwargs={'url': next_url})
		return reverse_lazy('index')


class AnalysisInfoView(TemplateView):
	''' Базовое представление страницы с информацией '''

	template_name = 'analysis/information.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'Analysis Info page'
		context['analyzer'] = Analyzer(context['url'])

		return context