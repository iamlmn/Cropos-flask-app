from flask import Flask,render_template,flash
import sys
from flask import flash

app = Flask(__name__)
app.secret_key = 'mypasswordis'

@app.route('/')
def homepage():
    return render_template('header.html')

@app.route('/dashboard/')
@app.route('/header/')
def dashpage():

    flash("flash test!!!!")
    flash("fladfasdfsaassh test!!!!")
    flash("asdfas asfsafs!!!!")
    return render_template('main.html')

'''@app.errorhandler(404)
def page_not_found():
    return render_template('error.html')
'''
if __name__ == "__main__":
    app.run()
