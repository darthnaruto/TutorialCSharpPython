from flask import Flask, json, make_response
app = Flask(__name__)

@app.route('/')
def home():
    response=make_response("<h1>Olá Mundo</h1><p>Eu sou o Eduardo</p>")
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

if __name__ == '__main__':
    app.run(debug=True)

