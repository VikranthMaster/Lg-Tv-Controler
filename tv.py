from click import launch
from pywebostv.discovery import *
from pywebostv.connection import *
from pywebostv.controls import *

store = {'client_key' : '601956a8f6e95dfd5202db3389fe1422'}

# client = WebOSClient.discover()[0]
client = WebOSClient('192.168.0.112')
client.connect()


for status in client.register(store):
    if status == WebOSClient.PROMPTED:
        print("please accept the connect to TV")
    elif status == WebOSClient.REGISTERED:
        print("Registration successful")
    else:
        print("Failed")

media = MediaControl(client)
# media.volume_up()
media.set_volume(20)
# media.pause()
# media.play()
# media.rewind()

print(media.get_volume())


system = SystemControl(client)
# system.notify('Hello World!')
# print(system.info())



app = ApplicationControl(client)
apps = app.list_apps()
# print(apps)

# netflix = [x for x in apps if "netflix" in x["title"].lower()][0]

# launch_info = app.launch(netflix)


yt = [x for x in apps if "youtube" in x["title"].lower()][0]

# launch_info = app.launch(yt)
launch_info = app.launch(yt, content_id="dQw4w9WgXcQ")

