from fabric.api import local, lcd

def prepare_deployment(branch_name):
    local('git add -A && git commit')
    local('git checkout master && git merge ' + branch_name)
