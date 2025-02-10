import os
from pathlib import Path
from decouple import config as decouple_config

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / 'templates'


SECRET_KEY = decouple_config("SECRET_KEY")

DEBUG = decouple_config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS  = ["0.0.0.0"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'quotes',
    'users',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql',
        "NAME": decouple_config("pg_database_name"),  
        "USER": decouple_config("pg_user"),
        "PASSWORD": decouple_config("pg_password"),
        "HOST": decouple_config('pg_host'),
        "PORT": decouple_config("pg_port"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


EMAIL_BACKEND = decouple_config('EMAIL_BACKEND')
EMAIL_HOST = decouple_config('EMAIL_HOST')
EMAIL_PORT = decouple_config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = decouple_config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = decouple_config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = decouple_config('EMAIL_HOST_PASSWORD')

# settings URL for reset  password
LOGIN_URL = 'users:room'  # URL by login
LOGIN_REDIRECT_URL = 'quotes:home'  # URL by redirect after login
LOGOUT_REDIRECT_URL = 'quotes:home'  # URL by refirect after logout

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
