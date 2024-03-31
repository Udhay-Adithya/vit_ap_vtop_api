from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def username():
    username = input("Enter your username : ")
    password = input("Enter your Password : ")

if __name__ == '__main__':
    app.run(debug=True)