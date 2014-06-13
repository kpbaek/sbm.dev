from fabric.api import local, lcd

def prepare_deployment(branch_name):
    local('git add -A && git commit')
    local('git checkout master && git merge ' + branch_name)
    
def deploy():
#    with lcd('/home/sbmkorea/public_html/plts.sbmkorea.com/'):
#    with lcd('D:/temp/test'):
#        local('rm -rf sbm')
#        local('git clone D:/temp/test/')
#    with lcd('/home/sbmkorea/public_html/plts.sbmkorea.com/sbm'):
    with lcd('D:/dev/python/web/sbm/sbm.dev'):
        local('python manage.py migrate plts')
        local('python manage.py collectstatic')
#        local('sudo service apache2 reload')
