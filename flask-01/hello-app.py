from flask import Flask

app = Flask(__name__)


# root directory
@app.route('/')
if __name__ == '__main__':
    app.run(debug=True)
