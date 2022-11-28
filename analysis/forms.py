from django import forms


class AnalysisForm(forms.Form):
	''' Форма ввода url для анализа '''

	url = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'URL...'}))