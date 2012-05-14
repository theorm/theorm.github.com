from fabric.api import *
from fabric.colors import green, red
import os

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader(__name__, 'templates'))

from app import personal

def check_requirement(command,install_text):
    failed = False
    with settings(warn_only=True):
        if not local('which %s' % command,capture=True):
            print red(install_text)
            failed = True
    if failed:
        abort("Fix dependencies and try again")

def compile_css():
    check_requirement('lessc','No "lessc" found. Install it with "npm install less@latest -g".')
    local('lessc -x static/css/styles.less > static/css/style.css')

def compile_page(path):
    template = env.get_template(path)
    page = template.render(personal=personal)
    
    dirname = os.path.dirname(path)
    if dirname and not os.path.exists(dirname):
        os.mkdir(dirname)
    f = open(path,'w')
    f.write(page)
    f.close()
    print 'compiled %s' % path

def compile_html():
    compile_page('index.html')
    compile_page('computers/index.html')

def compile():
    compile_css()
    compile_html()
    
def serve():
    local('python app.py')

    