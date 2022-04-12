# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&%q2glrc1x-_5_0=1c06o)^f5tpg+tsui(j^m0r5x^1q4qxv4n'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Celtics0314!!'
    }
}