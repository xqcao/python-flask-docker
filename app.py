from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def helloindex():
    return render_template('index.html', msg="hello flask")


@app.route('/new', methods=["POST"])
def add_new():
    newmsg = request.form['uname'] + "  "+str(datetime.datetime.now())
    print(newmsg)
    return render_template('index.html', msg=newmsg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
