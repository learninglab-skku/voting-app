# settings/local.py
from .base import *


DEBUG = True

# # Debug toolbar
# INSTALLED_APPS += ("debug_toolbar", )
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
# DEBUG_TOOLBAR_PATCH_SETTINGS = False
# DEBUG_TOOLBAR_CONFIG ={
#     'SHOW_TOOLBAR_CALLBACK': lambda x: True
# }

INTERNAL_IPS = ['127.0.0.1', '::1', '0.0.0.0']



# ALLOWED_HOSTS = ['192.168.0.2', '127.0.0.1']