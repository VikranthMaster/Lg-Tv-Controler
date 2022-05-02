from flask import Flask, redirect, url_for, flash
from flask import render_template, request
import tv
# from pywebostv.discovery import * #pip install pywebostv
# from pywebostv.connection import *
# from pywebostv.controls import *

app = Flask(__name__, template_folder='templates')
app.secret_key = 'knskand andjsnaj'

store = {'client_key': 'c146293fcc14626b469f11d5790f21c0'}

# client = WebOSClient("192.168.0.112")
# client.connect()
# for status in client.register(store):
#     if status == WebOSClient.PROMPTED:
#         print("Please accept the connect on the TV!")
#     elif status == WebOSClient.REGISTERED:
#         print("Registration successful!")

remote = tv.Remote(store,ip="192.168.0.112")

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        usr = request.form['vol']
        remote.set_vol(int(usr))
    elif request.method == "POST":
        msg = request.form['notify']
        remote.notify(f"{msg}")
    else:
        pass
    return render_template("index.html")

if __name__ == '__main__':  
   app.run(debug = True)  
