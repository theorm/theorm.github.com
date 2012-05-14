from flask import Flask, render_template
app = Flask(__name__)

personal = {
    'links' : {
        'cv'            : 'http://careers.stackoverflow.com/theorm',
        'github'        : 'http://github.com/theorm',
        'linkedin'      : 'http://au.linkedin.com/in/romankalyakin',
        'twitter'       : 'http://twitter.com/theorm',
        'email'         : 'roman@kalyakin.com',
        'telephone'     : '+61 423 809 868',
        'photography'   : 'http://theothermind.com/',
    },
    'projects' : {
        'Journeum'          : 'http://journeum.com',
        'The Property Pool' : 'http://thepropertypool.com',
    }
}

@app.route('/')
def index():
    return render_template('index.html',personal=personal)

@app.route('/computers')
def computers():
    return render_template('computers/index.html',personal=personal)

if __name__ == '__main__':
    app.run(debug=True)
