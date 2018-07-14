from fabric import task
from termcolor import colored
import os
from invoke import Exit

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader(__name__, 'templates'))


from app import personal

def green(*args):
    return colored(args, 'green')

def red(*args):
    return colored(args, 'red')

def check_requirement(c, command, install_text):
    if not c.local('which %s' % command, warn=True):
        print(red(install_text))
        raise Exit("Fix dependencies and try again")

@task
def compile_css(c):
    # check_requirement(c, 'lessc','No "lessc" found. Install it with "npm install less@latest -g".')
    c.local('/usr/local/bin/node /usr/local/bin/lessc -x static/css/styles.less > static/css/style.css')

@task
def compile_page(c, path):
    template = env.get_template(path)
    page = template.render(personal=personal)

    dirname = os.path.dirname(path)
    if dirname and not os.path.exists(dirname):
        os.mkdir(dirname)
    f = open(path,'w')
    f.write(page)
    f.close()
    print('compiled %s' % path)

@task
def compile_html(c):
    compile_page(c, 'index.html')
    compile_page(c, 'computers/index.html')
    compile_page(c, 'cv.html')

@task
def compile(c):
    compile_css(c)
    compile_html(c)

@task
def serve(c):
    c.local('python app.py')
