from fabric.api import lcd
from fabric.api import local

def prepare_deployment(branch_name):
  local('python manage.py test grcproj')
  local('git add -p && git commit')

def deploy():
  with lcd('~/djdev'):
  
  # With git..
   local('git pull /opt/django-projects/grcproj/')

   local('python manage.py test itms')
   local('python manage.py runserver 192.168.1.124:5555')

