# complete_project.wsgi is configured to live in projects/complete_project/deploy. 
# If you move this file you need to reconfigure the paths below.
import os 
import sys
# redirect sys.stdout to sys.stderr for bad libraries like geopy that uses 
# print statements for optional import exceptions. 
sys.path.append('C:/Documents and Settings/Syno-Frank/PycharmProjects')
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoPro.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()