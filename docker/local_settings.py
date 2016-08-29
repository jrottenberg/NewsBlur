import logging
import pymongo
import os

# ===================
# = Server Settings =
# ===================

ADMINS                = (
    ('Samuel Clay', 'samuel@newsblur.com'),
)

SERVER_EMAIL          = 'server@newsblur.com'
HELLO_EMAIL           = 'hello@newsblur.com'
NEWSBLUR_URL          = 'http://docker.newsblur.com'
SESSION_COOKIE_DOMAIN = '.newsblur.com'

# ===================
# = Global Settings =
# ===================

DEBUG = True
DEBUG_ASSETS = DEBUG
MEDIA_URL = '/media/'
SECRET_KEY = 'YOUR SECRET KEY'
AUTO_PREMIUM_NEW_USERS = True
AUTO_ENABLE_NEW_USERS = True

REDIS_HOST = os.environ.get('REDIS', 'redis')

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': REDIS_HOST + ':6379',
        'OPTIONS': {
            'DB': 6,
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Set this to the username that is shown on the homepage to unauthenticated users.
HOMEPAGE_USERNAME = 'popular'

# Google Reader OAuth API Keys
OAUTH_KEY = 'www.example.com'
OAUTH_SECRET = 'SECRET_KEY_FROM_GOOGLE'

S3_ACCESS_KEY = 'XXX'
S3_SECRET = 'SECRET'
S3_BACKUP_BUCKET = 'newsblur_backups'
S3_PAGES_BUCKET_NAME = 'pages-XXX.newsblur.com'
S3_ICONS_BUCKET_NAME = 'icons-XXX.newsblur.com'

STRIPE_SECRET = "YOUR-SECRET-API-KEY"
STRIPE_PUBLISHABLE = "YOUR-PUBLISHABLE-API-KEY"

# ===============
# = Social APIs =
# ===============

FACEBOOK_APP_ID = '111111111111111'
FACEBOOK_SECRET = '99999999999999999999999999999999'
TWITTER_CONSUMER_KEY = 'ooooooooooooooooooooo'
TWITTER_CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
YOUTUBE_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# =============
# = Databases =
# =============

DATABASES = {
    'default': {
        'NAME': 'newsblur',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': os.environ.get('DATABASE_USER', 'newsblur'),
        'PASSWORD': os.environ.get('DATABASE_PASS', 'newsblur'),
        'HOST': os.environ.get('DATABASE_HOST', 'postgres'),
        'OPTIONS': {
            "autocommit": True,
        },
    },
}

MONGO_DB = {
    'name': os.environ.get('MONGO_DB', 'newsblur'),
    'host': os.environ.get('MONGO_HOST', 'mongo'),
    'port': 27017
}

MONGO_ANALYTICS_DB = {
    'name': os.environ.get('MONGO_DB', 'analytics'),
    'host': os.environ.get('MONGO_HOST', 'mongo'),
    'port': 27017
}

MONGODB_SLAVE = {
    'host': os.environ.get('MONGO_HOST', 'mongo')
}

# Celery RabbitMQ/Redis Broker
BROKER_URL = "redis://" + REDIS_HOST + ":6379/0"
CELERY_RESULT_BACKEND = BROKER_URL

REDIS = {
    'host': REDIS_HOST,
}
REDIS_PUBSUB = {
    'host': REDIS_HOST,
}

REDIS_PUBSUB_POOL = {
    'host': REDIS_HOST,
}
REDIS_STORY = {
    'host': REDIS_HOST,
}
REDIS_SESSIONS = {
    'host': REDIS_HOST,
}
ELASTICSEARCH_FEED_HOSTS = os.environ.get('ELASTICSEARCH__HOSTS', 'elasticsearch:9200')
ELASTICSEARCH_STORY_HOSTS = os.environ.get('ELASTICSEARCH__HOSTS', 'elasticsearch:9200')

BACKED_BY_AWS = {
    'pages_on_node': False,
    'pages_on_s3': False,
    'icons_on_s3': False,
}

ORIGINAL_PAGE_SERVER = "127.0.0.1:3060"
REMOVE_WWW_FROM_DOMAIN = False


# ===========
# = Logging =
# ===========

# Logging (setup for development)
LOG_TO_STREAM = True

if len(logging._handlerList) < 1:
    LOG_FILE = '/opt/newsblur/logs/development.log'
    logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)-12s: %(message)s',
                            datefmt='%b %d %H:%M:%S',
                            handler=logging.StreamHandler)
