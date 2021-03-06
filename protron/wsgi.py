"""
WSGI config for protron project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

For more information, visit
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

# -*- coding: utf-8 -*-

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'protron.settings')

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()



#import os, sys
#sys.path.insert(0, '/var/www/u0748446/data/www/protron-2.ru/protron')
#sys.path.insert(1, '/var/www/u0748446/data/protronenv/lib/python3.7/site-packages')
#os.environ['DJANGO_SETTINGS_MODULE'] = 'protron.settings'
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()