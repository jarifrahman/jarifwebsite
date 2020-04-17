SECRET_KEY = 'e=p#@#t#uxhm3@2e#s(n+3$1f-qeus7wp$q%g=i5o*k6t$n00i'

ALLOWED_HOSTS = ['161.35.96.186']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfoliodb',
        'USER':'djangodbman',
        'PASSWORD':'django123',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

