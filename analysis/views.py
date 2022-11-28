from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import AnalysisForm


class AnalysisView(FormView):
	''' Базовое представление страцы с анализом '''

	template_name = 'analysis/analysis.html'
	form_class = AnalysisForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'AnalysisView'

		return context

	def post(self, request, *args, **kwargs):
		form = AnalysisForm(request.POST)
		print(form.data['url'])
		return super().post(request, *args, **kwargs)

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

		return context