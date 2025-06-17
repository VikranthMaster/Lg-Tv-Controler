from flask import Flask, render_template, request, redirect, url_for
from tv import *
from wakeonlan import send_magic_packet

app = Flask(__name__)


MAC = "44-CB-8B-2B-7E-DC"
IP = "192.168.1.35"
store = {'client_key': 'bd6b621e59cd9f6cde153e30190b1847'}

store1 = {}

rem = None

@app.route("/")
def home():
    global rem
    try:
        rem = Remote(token = store1, ip=IP)
    except:
        print("Not available")
    return render_template('index.html')

@app.route("/vol", methods = ["GET", "POST"])
def vol():
    if request.method == "POST":
        volume = request.form['vol']
        rem.set_vol(int(volume))
        return redirect(url_for('home'))  # redirect to home after setting volume
    return "404"

@app.route("/notify", methods = ["GET", "POST"])
def notify():
    if request.method == "POST":
        note = request.form['notify']
        rem.notify(note)
        return redirect(url_for('home'))  # redirect to home after setting volume
    return "404"

@app.route("/turnon", methods = ["GET","POST"])
def turnon():
    if request.method == "POST":
        send_magic_packet(MAC)
        return redirect(url_for('home'))
    return "404"

@app.route("/turnoff", methods =["GET", "POST"])
def turnoff():
    if request.method == "POST":
        rem.turnoff()
        return redirect(url_for('home'))
    return '404'

@app.route("/open", methods = ["GET", "POST"])
def open():
    if request.method == "POST":
        usr = request.form['open']
        print(rem.list_apps())
        rem.open_app(usr)
        return redirect(url_for('home'))
        
@app.route("/forward", methods = ["GET", "POST"])
def forward():
    if request.method == "POST":
        rem.fast_forward()
        return redirect(url_for('home'))

@app.route("/play", methods = ["GET", "POST"])
def play():
    if request.method == "POST":
        rem.play()
        return redirect(url_for('home'))


@app.route("/stop", methods = ["GET", "POST"])
def stop():
    if request.method == "POST":
        rem.stop()
        return redirect(url_for('home'))


@app.route("/backward", methods = ["GET", "POST"])
def backward():
    if request.method == "POST":
        rem.rewind()
        return redirect(url_for('home'))

@app.route("/pause", methods = ["GET", "POST"])
def pause():
    if request.method == "POST":
        rem.pause()
        return redirect(url_for('home'))


@app.route("/ok", methods = ["GET", "POST"])
def ok():
    if request.method == "POST":
        rem.ok()
        return redirect(url_for('home'))
    return '404'

@app.route("/up", methods = ["GET", "POST"])
def up():
    if request.method == "POST":
        rem.up()
        return redirect(url_for('home'))
    return '404'

@app.route("/down", methods = ["GET", "POST"])
def down():
    if request.method == "POST":
        rem.down()
        return redirect(url_for('home'))
    return '404'

@app.route("/left", methods = ["GET", "POST"])
def left():
    if request.method == "POST":
        rem.left()
        return redirect(url_for('home'))
    return '404'

@app.route("/right", methods = ["GET", "POST"])
def right():
    if request.method == "POST":
        rem.right()
        return redirect(url_for('home'))
    return '404'

@app.route("/back", methods = ["GET", "POST"])
def back():
    if request.method == "POST":
        rem.back()
        return redirect(url_for('home'))
    return '404'

@app.route("/menu", methods = ["POST", "GET"])
def menu():
    if request.method == "POST":
        rem.menu()
        return redirect(url_for('home'))
    return '404'


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)