#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
import sys
from collections import OrderedDict

sys.path.append(os.curdir)
from pugpb import members_of


AUTHOR = "PUG-PB"
SITENAME = "PUG-PB"
SITEURL = "https://pb.python.org.br"
PATH = "content"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

META_DESCRIPTION = """O PUG-PB é uma comunidade de usuários (profissionais e
                      amadores) da linguagem Python, onde prezamos pela troca de
                      conhecimento, respeito mútuo e diversidade (tanto de 
                      opinião quanto de tecnologias)."""

META_KEYWORDS = ["pug-pb", "python", "programação", "paraiba", "desenvolvimento"]

TIMEZONE = "America/Recife"
THEME = "themes/malt"
MALT_BASE_COLOR = "red"

SITE_LOGO = "images/logo/pug_logo.png"
SITE_LOGO_MOBILE = "images/logo/pug_logo.png"

STATIC_PATHS = ["images", "pdfs", "extra"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

WELCOME_TITLE = "Seja bem vindo ao {}!".format(SITENAME)
WELCOME_TEXT = "Grupo de usuários da linguagem Python na Paraíba."
SITE_BACKGROUND_IMAGE = "images/banners/Lajedo_pai_mateus_paraiba.jpg"
FOOTER_ABOUT = META_DESCRIPTION

DEFAULT_LANG = "pt"

ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"

CATEGORY_URL = "blog/categorias/{slug}"
CATEGORY_SAVE_AS = "blog/categorias/{slug}/index.html"
CATEGORIES_URL = "blog/categorias"
CATEGORIES_SAVE_AS = "blog/categorias/index.html"

TAG_URL = "blog/tags/{slug}"
TAG_SAVE_AS = "blog/tags/{slug}/index.html"
TAGS_URL = "blog/tags"
TAGS_SAVE_AS = "blog/tags/index.html"

AUTHOR_URL = "blog/autores/{slug}"
AUTHOR_SAVE_AS = "blog/autores/{slug}/index.html"
AUTHORS_URL = "blog/autores"
AUTHORS_SAVE_AS = "blog/autores/index.html"

INDEX_SAVE_AS = "blog/index.html"

PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ["./.plugins"]
PLUGINS = ["better_figures_and_images", "sitemap", "liquid_tags.youtube"]

RESPONSIVE_IMAGES = True
PYGMENTS_STYLE = "perldoc"
# PYGMENTS_STYLE = "friendly"
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.8, "indexes": 0.2, "pages": 0.7},
    "changefreqs": {"articles": "daily", "indexes": "daily", "pages": "monthly"},
}

GITHUB_REPO = "http://github.com/pug-pb/pug-pb-site"
GITHUB_BRANCH = "master"
# TWITTER = "@__pugpb__"
OPEN_GRAPH_IMAGE = "/images/logo/pug-logo.png"

# Navbar Links
NAVBAR_HOME_LINKS = [
    {"title": "Eventos", "href": "eventos.html",},
    {"title": "Comunidade", "href": "comunidade.html",},
    {"title": "Membros", "href": "membros.html",},
    {"title": "Blog", "href": "blog/index.html",},
]

NAVBAR_BLOG_LINKS = [
    {"title": "Categorias", "href": "blog/categorias/index.html",},
    {"title": "Autores", "href": "blog/autores/index.html",},
    {"title": "Tags", "href": "blog/tags/index.html",},
]

SOCIAL_LINKS = (
    {"href": "https://t.me/pugpb", "icon": "fa-paper-plane", "text": "Telegram",},
    {"href": "https://github.com/pug-pb", "icon": "fa-github", "text": "GitHub",},
    {"href": "https://twitter.com/pug_pb", "icon": "fa-twitter", "text": "Twitter",},
    {"href": "https://www.instagram.com/pug.pb/", "icon": "fa-instagram", "text": "Instagram",},
    {
        "href": "https://www.youtube.com/channel/UClTpIg2FFOCzDKtiEy3F9FA", 
        "icon": "fa-youtube", "text": "Youtube",},
    {
        "href": "https://www.facebook.com/pug-pb",
        "icon": "fa-facebook",
        "text": "Facebook",
    },
    {
        "href": "https://groups.google.com/forum/#!forum/pug-pb",
        "icon": "fa-envelope",
        "text": "Mailing List",
    },
)

MEMBROS = OrderedDict(members_of(["pug-pb", "PUG-PB-Traducao"]))

MALT_HOME = [
    {
        "color": "red lighten-5",
        "title": "O que Fazemos?",
        "items": [
            {
                "title": "Eventos",
                "icon": "fa-calendar-day",
                "text": "Os eventos que a comunidade organizou e os que "
                "estão programados pra acontecer. Informações, inscrições, "
                "submissões de palestras.",
                "buttons": [{"text": "Mais detalhes", "href": "eventos.html",},],
            },
            {
                "title": "Comunidade",
                "icon": "fa-comments",
                "text": "A comunidade do PUG-PB se comunica através da lista "
                "de email e do grupo no Telegram, mas frequentemente "
                "são promovidos encontros diversos, como reuniões de "
                "planejamento, meetups e oficinas. ",
                "buttons": [{"text": "Saiba Mais", "href": "comunidade.html",},],
            },
            {
                "title": "Membros",
                "icon": "fa-users",
                "text": "A comunidade do PUG-PB organiza eventos, mantém a "
                "comunicação ativa, divulga eventos, mantém redes "
                "sociais etc. ",
                "buttons": [{"text": "Conheça", "href": "membros.html",},],
            },
        ],
    },
]

EVENTO_PROGRAMADO = [
    {
        "color": "red lighten-5",
        "title": "Próximo Evento",
        "items": [
            {
                "title": "Nivelamento em Git",
                "icon": "fa-calendar-check",
                "text": "Preparando os trabalhos para o Grupo de Estudos",
                "date": "09/12/2020 19:00h",
                # "link": "https://bit.ly/pugpb-meetup",
                # "talks": "https://bit.ly/pugpb-talks",
                # "media": [
                #     "images/mv_2020_04_crop.jpg",
                #     "images/mv_2020_03_crop.jpg",
                #     "images/mv_2020_01_crop.jpg",
                #     "images/mv_2020_02_crop.jpg",
                # ],
            },
        ],
    },
]

EVENTOS_ANTERIORES = [
    {
        "color": "red lighten-5",
        "title": "Eventos Anteriores",
        "items": [
            {
                "title": "MeetUp Virtual 2020",
                "icon": "far fa-fire",
                "text": "Meetup virtual 2020, com a presença de "
                "Eduardo Mendes, entre outros ",
                # "buttons": [{"text": "Mais detalhes", "href": "#",},],
            },
            {
                "title": "Python Nordeste 2018",
                "icon": "far fa-sun",
                "text": "Conferência da comunidade Python Nordeste do ano "
                "de 2018, em Campina Grande-PB ",
                # "buttons": [{"text": "Mais detalhes", "href": "#",},],
            },
            {
                "title": "MeetUp PUG-PB Guarabira",
                "icon": "fa-book-open",
                "text": "Conferência da comunidade no Instituto Federal da "
                "cidade de Guarabira-PB, em 04/2018 ",
                # "buttons": [{"text": "Mais detalhes", "href": "#",},],
            },
            {
                "title": "MeetUp PUG-PB Rio Tinto",
                "icon": "fa-university",
                "text": "Conferência da comunidade no Campus da UFPB da cidade "
                "de Rio Tinto-PB, em 03/2018 ",
                # "buttons": [{"text": "Mais detalhes", "href": "#",},],
            },
        ],
    },
]

from themes.malt.functions import *
