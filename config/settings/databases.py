# from config.settings.base import env


# DATABASES = {
#     "default": env.db_url(
#         "DATABASE_URL", 
#         default="postgres://postgres:postgres@postgres:5432/uptime_robot",
#     )
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "uptime_robot",
        "HOST": "postgres",
        #"HOST": "postgres",
        "PORT": 5432,
        "USER": "postgres",
        'PASSWORD':'postgres',
        #'PASSWORD':'postgres',
    }
} 

# DATABASES = {
#     "default": {
#         "NAME": "uptime_robot",
#         "USER": "postgres",
#         'PASSWORD':'postgres',
#         "HOST": "postgres",
#         "PORT": 5432,
#         "ENGINE": "django.db.backends.postgresql",
#     }
# } 