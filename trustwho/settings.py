# coding: utf-8
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.utils.translation import gettext_lazy as _
"""
Django settings for trustwho project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_abs(path):
    return os.path.join(BASE_DIR, path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5o6bn-lljhwz#m6od%8y5ipq#@wi_7_81165j0*-kzbd85@(oa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
WECHATDEBUG = False


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'djcelery',
    'django_extensions',
    'flattext',
    'easy_thumbnails',
    'common',
    'bigvs',
    'articles',
    'wechat',
    'feedback',
    'subscribe',
    'accessrecord',
    'prediction',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'common.middleware.RecordEventMiddleWare',
    'common.middleware.WechatUserMiddleWare',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

ROOT_URLCONF = 'trustwho.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            get_abs('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

WSGI_APPLICATION = 'trustwho.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wealth_db',
        'HOST': 'rdsw5ilfm0dpf8lee609.mysql.rds.aliyuncs.com',
        'PORT': 3306,
        'USER': 'licj',
        'PASSWORD': 'AAaa_0504'
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'django_cache_table',
#     }
# }
  
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': 'redis://:redis7890@localhost:6379/0',
        "OPTIONS": {
            'DB': 0,
            'PASSWORD': 'redis7890',
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        },
    },
}
REDIS_TIMEOUT = 7 * 24 * 60 * 60
CUBES_REDIS_TIMEOUT = 60 * 60
NEVER_REDIS_TIMEOUT = 365 * 24 * 60 * 60
SITE_REDIS_TIMEOUT = 60


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    get_abs('static'),
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': get_abs('logs/debug.log'),
            'formatter': 'verbose',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'debug': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
        }
    }
}

# django_sult config
SUIT_CONFIG = {
    'ADMIN_NAME': '信谁微信后台管理',
    
    'MENU_ICONS': {
        'sites': 'icon-leaf',
    },
        
    'MENU': (
        'sites',
        # Rename app and set icon
        {'app': 'wechat', 'label': _(u'微信管理'), 'icon':'icon-user'},
        {'app': 'bigvs', 'label': _(u'大V管理'), 'icon':'icon-heart'},
        {'app': 'articles', 'label': _(u'文章管理'), 'icon':'icon-list-alt'},
        {'app': 'prediction', 'label': _(u'大V风向'), 'icon':'icon-calendar'},
        {'app': 'feedback', 'label': _(u'意见反馈'), 'icon':'icon-edit'},
        {'app': 'accessrecord', 'label': _(u'访问记录'), 'icon':'icon-list'},
        {'app': 'djcelery', 'label': _(u'定时任务'), 'icon':'icon-bell'},
        {'app': 'flattext', 'label': _(u'flattext'), 'icon':''},
        {'label': _(u'系统用户设置'), 'icon': 'icon-cog', 'models': ('auth.user', 'auth.group')},
    )
    
    
}

# 微信公众号配置
WECHAT_APPID = 'wx3e332c31920ab2da'
WECHAT_APPSECRET = '8313b9bda1d9bf2d7eee9ea0668e4a9d'
WECHAT_TOKEN = 'B0quTechWebchat'

# djcelery+broker配置
BROKER_URL = 'redis://:redis7890@127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://:redis7890@127.0.0.1:6379/0'
REDIS_CONNECT_RETRY = True
CELERY_TASK_RESULT_EXPIRES = 10
import djcelery
djcelery.setup_loader()

SOUTH_MIGRATION_MODULES = {
    'djcelery': 'djcelery.south_migrations',
}
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

CELERY_TIMEZONE = TIME_ZONE

# shell_plus
SHELL_PLUS_PRE_IMPORTS = (
    ('articles.tasks', 'build_score'),
)

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (54, 54), 'crop': True},
    },
}