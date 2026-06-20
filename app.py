from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Mr. Razib welcome to CI/CD project. CI/CD Pipeline Working Successfully..! Thank yo..! Jenkins Login Info is : Admin, Admin123"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
