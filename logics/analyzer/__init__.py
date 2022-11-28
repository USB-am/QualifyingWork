class Analyzer:
	''' Предоставляет методы для анализа сайта '''
	title = 'title'
	metas = ['meta1', 'meta2']

	def __init__(self, url: str):
		self.url = url