url = 'https://vk.com'


# === SITE === #
site = Site(domain=url)

# Favicon
print(site.favicon.href)

# Meta
print(site.meta.description)

# Map
'''
site_map = {
	domain: [
		{'music': []},
		{'message': []},
		{'video': []},
		{'<slug:str>': [ ??? ]},
	],
}
'''
print(site.site_map)	# dict

# === SITE === #


# === PAGE === #
page = Page(url=url)


# === PAGE === #