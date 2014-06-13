from fabric.api import local, lcd

def prepare_deployment(branch_name):
    local('git add -A && git commit')
    local('git checkout master && git merge ' + branch_name)
    
def deploy():
    with lcd('/home/sw3/public_html/plts.sbmkorea.com/'):
        local('rm -rf sbm')
#        local('git clone /home/sbmkorea/DJANGO_ENV/projects/sbm/')
    with lcd('/home/sw3/public_html/plts.sbmkorea.com/sbm'):
        local('python manage.py migrate plts')
        local('python manage.py collectstatic')
        local('sudo service apache2 reload')
