from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    first_name = 'Gamdo'
    Sent = "This is some <h1>tsufb</h1>"
    candy = ['Orange', 'chocolate', 13]
    return render_template('index.html', first=first_name, Sent=Sent, candy=candy)

@app.route('/user/<name>')
def user(name):
    return render_template('users.html', Users=name)

@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(err):
    return render_template('500.html'), 404

if __name__ == '__main__':
    app.run(debug=True)