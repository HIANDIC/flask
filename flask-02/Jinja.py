from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def head():
    return render_template('index.html', number1=17, number2=10)


@app.route('/mult')
def number():
    x = 7
    y = 11

    return render_template('body.html', num1=x, num2=y, mult=x*y)


if __name__ == '__main__':

    # for local hosting
    #app.run(port=80, debug=True)

    # for hosting web not local
    app.run(host='0.0.0.0', port=80)
