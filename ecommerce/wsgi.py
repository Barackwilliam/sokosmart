
# Kwa project zingine kama hizi au mifumo mbalimbali ya 
# kusimamia biashara na shughuli zingine nitafute kwa mawasiliano haya
# phone: 0629712678
# Email: barackwilliam12@gmail.com
# Whatsaap: 0629712678

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

application = get_wsgi_application()
