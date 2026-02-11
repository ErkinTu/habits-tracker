# Основной файл конфигурации Django проекта
import logging
# Импорт библиотек
from pathlib import Path
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ безопасности проекта
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is not set in environment")

# Режим отладки
# Для разработки (dev) - True, для production - False
DEBUG = os.getenv("DEBUG", "False").strip().lower() in {"1", "true", "yes", "on"}

# Список разрешенных hosts от которых мы можем принимать запросы
ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",") if h.strip()]

# Кастомная модель пользователя (заменяет django.contrib.auth.models.User)
AUTH_USER_MODEL = "accounts.User"

# Список встроенных Django приложений
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

# Список сторонних приложений
THIRD_PARTY_APPS = [
    "rest_framework",
    'rest_framework.authtoken',
    "rest_framework_simplejwt",
    "drf_spectacular",
    "corsheaders",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "dj_rest_auth",
    "dj_rest_auth.registration",
]

# Список локальных приложений
LOCAL_APPS = [
    "accounts",
    "habits",
]

# Общий список приложений
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Список middleware для обработки запросов
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# Корневой url файл проекта
ROOT_URLCONF = 'server.urls'

# Конфигурация шаблонов Django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'

# Конфигурация базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        # Атомарность на уровне HTTP-запроса: каждый запрос выполняется в транзакции
        'ATOMIC_REQUESTS': True,
    }
}

# Валидаторы паролей
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

# Настройка интернациональности
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Настройка статических файлов
STATIC_URL = 'static/' # URL статики
STATIC_ROOT = BASE_DIR / 'staticfiles' # Путь для собранных файлов статики

# Настройки Django REST Framework (DRF)
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication", # Идентификация пользователя по JWT-токену в заголовке
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        # "rest_framework.permissions.IsAuthenticated", # Доступ только для авторизованных пользователей
        "rest_framework.permissions.AllowAny", # Публичный доступ ко всем эндпоинтам
    ),
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.AnonRateThrottle", # Ограничение запросов для анонимных пользователей
    ),
    "DEFAULT_THROTTLE_RATES": {
        "anon": "100/day", # Лимит запросов для анонимных пользователей
    },
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer", # Рендеринг в JSON
    ),
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser", # Парсинг JSON-данных
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema", # Генерация OpenAPI
}

# Генерация OpenAPI-схемы (Swagger/ReDoc) и метаданные API
SPECTACULAR_SETTINGS = {
    "TITLE": "Habits Tracker API",
    "VERSION": "0.1.0",
}

# ID объекта Site из django.contrib.sites.
# Нужен для django-allauth/dj-rest-auth: домен, формирование ссылок в письмах и т.п.
SITE_ID = 1


# Настройки CORS для dev и prod
if DEBUG:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
else:
    # Добавить реальные домены frontend в production
    CORS_ALLOWED_ORIGINS = []

# Базовые настройки безопасности
SECURE_CONTENT_TYPE_NOSNIFF = True # Запрещает MIME-sniffing
X_FRAME_OPTIONS = "DENY" # Защита от Clickjacking

# Настройка логирования
LOG_LEVEL = "DEBUG" if DEBUG else "INFO"
LOG_FILE = BASE_DIR / "debug.log"  # Общий лог-файл проекта

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": { # Форматирование
        "standard": {
            "format": "%(asctime)s | %(levelname)s | %(name)s:%(lineno)d | %(message)s",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": LOG_LEVEL,
            "formatter": "standard",
        },
        "file": {
            # Защита от бесконечного роста файла
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "standard",
            "filename": str(LOG_FILE),
            "maxBytes": 10 * 1024 * 1024,  # 10MB
            "backupCount": 5,
        },
    },

    # root ловит всё "мимо" именованных логгеров
    "root": {
        "handlers": ["console"] if DEBUG else ["file"],
        "level": LOG_LEVEL,
    },

    "loggers": {
        # Базовые логи Django
        "django": {
            "handlers": ["console"] if DEBUG else ["file"],
            "level": "INFO",
            "propagate": False,
        },
        # 500 ошибки запросов
        "django.request": {
            "handlers": ["console"] if DEBUG else ["file"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}