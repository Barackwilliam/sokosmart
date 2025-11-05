



# Kwa project zingine kama hizi au mifumo mbalimbali ya 
# kusimamia biashara na shughuli zingine nitafute kwa mawasiliano haya
# phone: 0629712678
# Email: barackwilliam12@gmail.com
# Whatsaap: 0629712678

import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
