import os
AUTHOR = 'Tales Mota'
SITENAME = 'Tales Mota'
SITEURL = 'https://talesmota.dev/'
# SITEURL = "http://localhost:8000"
# PORT=8000
# 
# RELATIVE_URLS = True
OUTPUT_PATH = 'docs'

PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'

THEME = "./theme/pelican-striped-html5up"
# THEME = "/home/tales/pelican-themes/brutalist/brutalist"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'
PLUGIN_PATHS = ['/home/tales/pelican-plugins']

MARKDOWN =  {
    'extensions' : ['codehilite', 'extra'],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

SEO_REPORT = True  # To enable this feature
SEO_ENHANCER = False  # To disable this feature
SEO_ENHANCER_OPEN_GRAPH = False # The default value for this feature
SEO_ENHANCER_TWITTER_CARDS = False # The default value for this feature    

SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('github', 'http://github.com/talesmota'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = [ 'pages']
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
GOOGLE_ANALYTICS=True