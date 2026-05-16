from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Mr. Razib welcome to CI/CD project. CI/CD Pipeline Working Successfully..! Thank you"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
