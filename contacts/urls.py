from django.urls import path

from .views import ContactsView


urlpatterns = [
	path('', ContactsView.as_view(), name='contacts'),
]