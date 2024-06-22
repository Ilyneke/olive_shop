import os

from environs import Env

env = Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORAGE_DIR = os.path.join(BASE_DIR, 'storage')

ALLOW_ORIGINS = env.list('ALLOW_ORIGINS', default=['*'])
ALLOW_CREDENTIALS = env.bool('ALLOW_CREDENTIALS', default=True)
ALLOW_METHODS = env.list('ALLOW_METHODS', default=['*'])
ALLOW_HEADERS = env.list('ALLOW_HEADERS', default=['*'])
EXPOSE_HEADERS = env.list('EXPOSE_HEADERS', default=['*'])

DOMAIN = env.str('DOMAIN')
API_DOMAIN = env.str('API_DOMAIN')
ADMIN_URL = DOMAIN + '/admin/login'

# Доступ в панель администратора
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
ALGORITHM = 'HS256'
AUTH_TOKEN = env.str('AUTH_TOKEN')
AUTH_SALT = env.str('AUTH_SALT')
HASH_PASSWORD = env.str('HASH_PASSWORD')
PASSWORD = env.str('PASSWORD', 'secret')
SHOP_ID = env.str('SHOP_ID')
SHOP_SECRET_KEY = env.str('SHOP_SECRET_KEY')
# openssl rand -hex 32
SECRET_KEY = env.str('SECRET_KEY')
ADMIN_USERNAME = env.str('AUTH_USERNAME')
