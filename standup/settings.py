import os

from standup.utils import truthiness

# Application settings.
# To override the values, create a local_settings.py and enter the
# new values there.

DEBUG = truthiness(os.environ.get('DEBUG', False))

# The key used to authenticate API calls.
API_KEY = os.environ.get('API_KEY', 'qwertyuiopasdfghjklzxcvbnm1234567890')

BLUEPRINTS = (
    'standup.apps.api.views',
    'standup.apps.landings.views',
    'standup.apps.status.views',
    'standup.apps.users.views',
)

SITE_URL = os.environ.get('SITE_URL', 'http://127.0.0.1:5000')
SITE_TITLE = os.environ.get('SITE_TITLE', 'standup')

SESSION_SECRET = os.environ.get('SESSION_SECRET',
                                'asdfghjklqwertyuiopzxcvbnm1234567890')

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///standup_app.db')

try:
    from local_settings import *
except ImportError:
    pass
