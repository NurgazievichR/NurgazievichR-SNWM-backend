from datetime import timedelta
from decouple import config


SIMPLE_JWT = {
    # 'ACCESS_TOKEN_LIFETIME': timedelta(days=int(config('ACCESS_TOKEN_LIFETIME'))),
    # 'REFRESH_TOKEN_LIFETIME': timedelta(days=int(config('REFRESH_TOKEN_LIFETIME'))),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=90),
    # чтобы при получении нового access токена, refresh тоже менялся
    'ROTATE_REFRESH_TOKENS': True,
    # чтобы уже существовавшие refresh токены снова не генерились
    'BLACKLIST_AFTER_ROTATION': True,

    "AUTH_HEADER_TYPES": ("Bearer",),
}