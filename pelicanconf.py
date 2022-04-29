AUTHOR = 'Tales Mota'
SITENAME = 'Tales Mota'
# SITEURL = 'https://talesmota.github.io/dev/'
SITEURL = 'http://localhost:8000/'
PORT=8000

# RELATIVE_URLS = True
OUTPUT_PATH = 'docs'

PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

THEME = "./theme/pelican-striped-html5up"
# THEME = "/home/tales/pelican-themes/brutalist/brutalist"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'
PLUGIN_PATHS = ['/home/tales/pelican-plugins']
PLUGINS = ['ace_editor']
ACE_EDITOR_PLUGIN={}
MARKDOWN =  {
    'extensions' : ['codehilite', 'extra'],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
    
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