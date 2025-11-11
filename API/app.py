from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/about')
def about():
    return "This is the About Page."

@app.route('/contact')
def contact():
    return "Contact us at contact@example.com"

@app.route('/services')
def services():
    return "We offer Web, Network, and Cloud Security services."

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}! Welcome to our Flask app."

if __name__ == '__main__':
    app.run(debug=True)
