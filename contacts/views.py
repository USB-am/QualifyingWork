from django.shortcuts import render
from django.views.generic import TemplateView


class ContactsView(TemplateView):
	''' Базовое представление страницы с контактной информацией '''

	template_name = 'contacts/contacts.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['title'] = 'Contacts information'

		return context