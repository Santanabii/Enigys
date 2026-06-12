# core/settings.py
import os
import dj_database_url
from dotenv import load_dotenv
from urllib.parse import urlparse
from pathlib import Path

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# In development, use a default key. ALWAYS set SECRET_KEY in environment variables for production!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-dev-key-change-this-in-production')
if os.getenv('SECRET_KEY') is None and not os.getenv('DEBUG', 'False') == 'True':
    raise ValueError(
        "SECRET_KEY environment variable must be set for production. "
        "Generate one with: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'"
    )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Parse ALLOWED_HOSTS from string to list
ALLOWED_HOSTS = [host.strip() for host in os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',') if host.strip()]

# Also add your Render URL
RENDER_URL = os.getenv('RENDER_EXTERNAL_URL', '').replace('https://', '').replace('http://', '').strip()
if RENDER_URL:
    ALLOWED_HOSTS.append(RENDER_URL)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rfq',
    'contacts',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'

# DATABASE CONFIGURATION - Important for Render
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}",
        conn_max_age=600,
        # For Render Internal URL - SSL is handled internally
        ssl_require=False if not DEBUG else False,
        # For Render External URL (if you must use it):
        # ssl_require=True
    )
}

# Fix for Render's internal database connections
# This ensures the database URL is parsed correctly
if 'DATABASE_URL' in os.environ:
    db_url = os.environ['DATABASE_URL']
    # Remove ?sslmode=require if present for internal connections
    if '?sslmode=require' in db_url and '-a.' not in db_url:
        db_url = db_url.split('?')[0]
        os.environ['DATABASE_URL'] = db_url

# CORS Configuration
# Helper function to parse comma-separated env vars safely
def parse_env_list(env_var: str, default: str = '') -> list:
    """Parse comma-separated environment variable into a list, filtering empty strings."""
    value = os.getenv(env_var, default)
    return [item.strip() for item in value.split(',') if item.strip()]

# Start with environment-provided origins
CORS_ALLOWED_ORIGINS = parse_env_list('CORS_ALLOWED_ORIGINS')

# Add Vercel frontend if VERCEL_URL is set
VERCEL_URL = os.getenv('VERCEL_URL', '').strip()
if VERCEL_URL:
    CORS_ALLOWED_ORIGINS.append(f'https://{VERCEL_URL}')
    CORS_ALLOWED_ORIGINS.append(f'https://{VERCEL_URL}.vercel.app')

# Add Render frontend URL from environment variable
RENDER_FRONTEND_URL = os.getenv('RENDER_FRONTEND_URL', '').strip()
if RENDER_FRONTEND_URL:
    CORS_ALLOWED_ORIGINS.append(f'https://{RENDER_FRONTEND_URL}')

# Add development URLs (safe for local testing)
CORS_ALLOWED_ORIGINS.extend([
    'http://localhost:5173',
    'http://localhost:3000',
])

# CSRF Trusted Origins (important for POST requests from frontend)
CSRF_TRUSTED_ORIGINS = parse_env_list('CSRF_TRUSTED_ORIGINS')
CSRF_TRUSTED_ORIGINS.extend([
    'https://*.vercel.app',
    'http://localhost:5173',
    'http://localhost:3000',
])

# If RENDER_FRONTEND_URL is set, add it to CSRF_TRUSTED_ORIGINS
if RENDER_FRONTEND_URL:
    CSRF_TRUSTED_ORIGINS.append(f'https://{RENDER_FRONTEND_URL}')

# Allow credentials (cookies, authorization headers)
CORS_ALLOW_CREDENTIALS = True

# Additional CORS settings for better security
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise configuration for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True