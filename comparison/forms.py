from django import forms


class ComparisonForm(forms.Form):
	''' Форма ввода url'ов для сравнения '''

	url_1 = forms.CharField(widget=forms.TextInput(
		attrs={'placeholder': 'Сompared web page url...'}
	))
	url_2 = forms.CharField(widget=forms.TextInput(
		attrs={'placeholder': 'Web page - comparer url...'}
	))