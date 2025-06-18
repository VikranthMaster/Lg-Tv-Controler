from flask import Flask, render_template, request, redirect, url_for
from tv import *
from wakeonlan import send_magic_packet

app = Flask(__name__)

MAC = "44:CB:8B:2B:7E:DC"
IP = "192.168.1.35"
store = {}
rem = None 

def connect_remote():
    global rem
    if rem is None:
        try:
            rem = Remote(token=store, ip=IP)
            return True
        except Exception as e:
            print(f"[!] Remote connection failed: {e}")
            rem = None
            return False
    return True

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/vol", methods=["POST"])
def vol():
    if connect_remote():
        try:
            volume = int(request.form['vol'])
            rem.set_vol(volume)
        except Exception as e:
            print(f"[!] Volume error: {e}")
    return redirect(url_for('home'))

@app.route("/notify", methods=["POST"])
def notify():
    if connect_remote():
        try:
            note = request.form['notify']
            rem.notify(note)
        except Exception as e:
            print(f"[!] Notify error: {e}")
    return redirect(url_for('home'))

@app.route("/turnon", methods=["POST"])
def turnon():
    send_magic_packet(MAC, ip_address=IP)
    return redirect(url_for('home'))

@app.route("/turnoff", methods=["POST"])
def turnoff():
    if connect_remote():
        try:
            rem.turnoff()
        except Exception as e:
            print(f"[!] Turnoff error: {e}")
    return redirect(url_for('home'))

@app.route("/open", methods=["POST"])
def open():
    if connect_remote():
        try:
            usr = request.form['open']
            print(rem.list_apps())
            rem.open_app(usr)
        except Exception as e:
            print(f"[!] Open app error: {e}")
    return redirect(url_for('home'))

@app.route("/forward", methods=["POST"])
def forward():
    if connect_remote():
        try:
            rem.fast_forward()
        except:
            pass
    return redirect(url_for('home'))

@app.route("/play", methods=["POST"])
def play():
    if connect_remote():
        try:
            rem.play()
        except:
            pass
    return redirect(url_for('home'))

@app.route("/stop", methods=["POST"])
def stop():
    if connect_remote():
        try:
            rem.stop()
        except:
            pass
    return redirect(url_for('home'))

@app.route("/backward", methods=["POST"])
def backward():
    if connect_remote():
        try:
            rem.rewind()
        except:
            pass
    return redirect(url_for('home'))

@app.route("/pause", methods=["POST"])
def pause():
    if connect_remote():
        try:
            rem.pause()
        except:
            pass
    return redirect(url_for('home'))

@app.route("/ok", methods=["POST"])
def ok():
    if connect_remote():
        try:
            rem.ok()
        except:
            pass
    return redirect(url_for('home'))

@app.route("/up", methods=["POST"])
def up():
    if connect_remote():
        try:
            rem.up()
        except:
            pass
    return redirect(url_for('home'))

@app.route("/down", methods=["POST"])
def down():
    if connect_remote():
        try:
            rem.down()
        except:
            pass
    return redirect(url_for('home'))

@app.route("/left", methods=["POST"])
def left():
    if connect_remote():
        try:
            rem.left()
        except:
            pass
    return redirect(url_for('home'))

@app.route("/right", methods=["POST"])
def right():
    if connect_remote():
        try:
            rem.right()
        except:
            pass
    return redirect(url_for('home'))

@app.route("/back", methods=["POST"])
def back():
    if connect_remote():
        try:
            rem.back()
        except:
            pass
    return redirect(url_for('home'))

@app.route("/menu", methods=["POST"])
def menu():
    if connect_remote():
        try:
            rem.menu()
        except:
            pass
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
