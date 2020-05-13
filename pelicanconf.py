#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
import sys
from collections import OrderedDict

sys.path.append(os.curdir)

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
SITE_BACKGROUND_IMAGE = "images/banners/por-do-sol.jpg"
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

GITHUB_REPO = "http://github.com/pug-pb/pug-pb.github.io"
GITHUB_BRANCH = "pelican"
# TWITTER = "@__pugpb__"
OPEN_GRAPH_IMAGE = "/images/logo/pug-logo.png"

# Navbar Links
NAVBAR_HOME_LINKS = [
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

MEMBROS = OrderedDict(
    (
        (
            "Fernando",
            {
                "email": "junio.webmaster@gmail.com",
                "linkedin": "fernand-junio",
                "github": "junioweb",
            },
        ),
        (
            "Hildeberto",
            {
                "email": "hildeberto@gmail.com",
                "twitter": "@__hilam__",
                "github": "hilam",
                "linkedin": "hildeberto",
                "site": {"nome": "H1L4M", "href": "http://hilam.github.io",},
            },
        ),
        ("Emanuel", {"linkedin": "emanuel-gomes-ferreira", "github": "emanuel-gomes"}),
        ("Janaína", {"email": "janagaliza@gmail.com",}),
        (
            "Newton",
            {
                "email": "newtonjgaliza@gmail.com",
                "linkedin": "newton-galiza-64108766",
                "twitter": "@NewtonGaliza",
                "github": "NewtonGaliza",
            },
        ),
        ("Allisson", {"linkedin": "allisson", "github": "allisson"}),
        (
            "Gustavo",
            {
                "linkedin": "gustavo-diniz-monteiro-9077b2133",
                "github": "GustavoDinizMonteiro",
            },
        ),
    )
)

MALT_HOME = [
    {
        "color": "red lighten-5",
        "title": "O que Fazemos?",
        "items": [
            {
                "title": "Comunidade",
                "icon": "fa-comments",
                "text": "A comunidade do PUG-PB se comunica através da lista "
                "de email e do grupo no telegram, mas frequentemente "
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
            {
                "title": "Projetos",
                "icon": "fa-briefcase",
                "text": "O principal projeto atual do PUG-PB é a organização "
                "da conferência Python Nordeste 2018, que se realizará "
                "de 24 a 26 de maio, em Campina Grande.",
                "buttons": [{"text": "Mais detalhes", "href": "projetos.html",},],
            },
        ],
    },
]

from themes.malt.functions import *
