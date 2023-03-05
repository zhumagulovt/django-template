from .base import env

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
