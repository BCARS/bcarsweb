
# Change this to False when deploying
# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['.bcars.org', 'localhost']
# Make these unique, and don't share it with anybody.
SECRET_KEY = "longuuidsecret"
NEVERCACHE_KEY = "anotherlonguuidsecret"

# 2.5MB - 2621440
# 5MB -     5242880
# 10MB -   10485760
# 20MB -   20971520
# 50MB -   52428800
# 100MB - 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = "52428800"
FILEBROWSER_MAX_UPLOAD_SIZE = MAX_UPLOAD_SIZE

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/mezzanine_debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

BLOG_SLUG = "logbook"
EVENT_SLUG = "events"

# This works for development, update for production (use a real db)
DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
