#!/usr/bin/python
import os, sys
sys.path.append('/path/to/your/django/projects/folder')
sys.path.append('/path/to/your/project/folder')
os.environ['DJANGO_SETTINGS_MODULE'] = 'projectName.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()