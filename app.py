from flask import Flask

app = Flask(__name__)

@app.get('/')
def function():
    return "Hello World"

if __name__ == '__main__':
    app.run()

  