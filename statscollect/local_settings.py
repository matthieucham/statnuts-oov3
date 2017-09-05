import os
from .settings import *

LOCAL_SETTINGS = True

if ON_OPENSHIFT:
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['*']
    DATABASES = {
        'default': {
            'NAME': 'statnuts',
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': os.getenv('OPENSHIFT_POSTGRESQL_DB_USERNAME'),
            'PASSWORD': os.getenv('OPENSHIFT_POSTGRESQL_DB_PASSWORD'),
            'HOST': os.getenv('OPENSHIFT_POSTGRESQL_DB_HOST'),
            'PORT': os.getenv('OPENSHIFT_POSTGRESQL_DB_PORT'),
            }
    }
else:
    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = []
    DATABASES = {
		'default': {
			'NAME': 'statscollect',
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'USER': 'postgres',
			'PASSWORD': 'root'
		}
	}

PHANTOMJS_BIN_PATH = os.path.join(os.getenv('OPENSHIFT_DATA_DIR'), 'phantomjs', 'bin', 'phantomjs')
PHANTOMJS_LOG_PATH = os.path.join(os.getenv('OPENSHIFT_LOG_DIR'), 'ghostdriver.log')

