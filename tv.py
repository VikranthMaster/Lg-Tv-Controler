from pywebostv.discovery import * #pip install pywebostv
from pywebostv.connection import *
from pywebostv.controls import *
from pprint import pprint
import json

# store = {'client_key' : #}
# store = {'client_key': 'TOKEN'}

class Remote(object):
    def __init__(self, token=None, client=None, ip=None):
        self.token = token
        self.ip = ip

        # Connect to TV
        if self.ip is not None:
            self.client = WebOSClient(self.ip)
        else:
            discovered = WebOSClient.discover()
            if not discovered:
                raise Exception("No TVs found on network.")
            self.client = discovered[0]

        self.client.connect()

        # Load token if available from file
        if self.token is None:
            try:
                with open("client_key.json", "r") as f:
                    self.token = json.load(f)
            except FileNotFoundError:
                self.token = None

        # Register with TV (shows popup on TV for first time)
        for status in self.client.register(self.token):
            if status == WebOSClient.REGISTERED:
                print("✅ Registration successful")
            elif status == WebOSClient.PROMPTED:
                print("📺 Please approve connection on the TV")
            elif status == WebOSClient.DENIED:
                raise Exception("❌ Registration denied by TV")

        with open("client_key.json", "w") as f:
            json.dump(self.token, f)
            

    def set_vol(self, vol=None):
        media = MediaControl(self.client)
        self.vol = vol
        if self.vol != None:
            media.set_volume(self.vol)
        else:
            pass

    def pause(self):
        media = MediaControl(self.client)
        media.pause()
    
    def play(self):
        media = MediaControl(self.client)
        media.play()
    
    def vol_up(self):
        media = MediaControl(self.client)
        media.volume_up()
    
    def get_vol_info(self):
        media = MediaControl(self.client)
        print(media.get_volume())
    
    def stop(self):
        media = MediaControl(self.client)
        media.stop()
    
    def rewind(self):
        media = MediaControl(self.client)
        media.rewind()
    
    def fast_forward(self):
        media = MediaControl(self.client)
        media.fast_forward()
    
    def notify(self, msg):
        self.msg = msg
        system = SystemControl(self.client)
        system.notify(self.msg)
    
    def turnoff(self):
        system = SystemControl(self.client)
        system.screen_off()
    
    def turnon(self):
        system = SystemControl(self.client)
        system.screen_on()
    
    def list_apps(self):
        app = ApplicationControl(self.client)
        apps = app.list_apps()
        pprint(apps)
    
    def open_app(self, name):
        self.name = name
        app = ApplicationControl(self.client)
        apps = app.list_apps()

        app_name = [x for x in apps if self.name in x["title"].lower()][0]

        launch_info = app.launch(app_name)
        return launch_info
    
    def close_app(self, launch_info):
        self.launch_info = launch_info
        app = ApplicationControl(self.client)
        app.close(self.launch_info)
    
    def get_app(self):
        app = ApplicationControl(self.client)
        app_id = app.get_current()
        apps = app.list_apps()
        foreground_app = [x for x in apps if app_id == x["id"]][0]
        icon_url = foreground_app["icon"]
        
        if "yt" in icon_url:
            print("Seeing Youtube")
        
        elif "SMALL_APP_ICON" in icon_url:
            print("Seeing Netflix")
        
        elif "aix_white" in icon_url:
            print("Seeing Prime Videos")

    def ok(self):
        inp = InputControl(self.client)
        inp.connect_input()
        inp.ok()
        
    def up(self):
        inp = InputControl(self.client)
        inp.connect_input()
        inp.up()
    
    def down(self):
        inp = InputControl(self.client)
        inp.connect_input()
        inp.down()
        
    def left(self):
        inp = InputControl(self.client)
        inp.connect_input()
        inp.left()
        
    def right(self):
        inp = InputControl(self.client)
        inp.connect_input()
        inp.right()
        
    def back(self):
        inp = InputControl(self.client)
        inp.connect_input()
        inp.back()
    
    def menu(self):
        inp = InputControl(self.client)
        inp.connect_input()
        inp.home()
