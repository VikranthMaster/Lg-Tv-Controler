from pywebostv.discovery import * #pip install pywebostv
from pywebostv.connection import *
from pywebostv.controls import *
from pprint import pprint

# store = {'client_key' : #}
# store = {'client_key': 'TOKEN'}

class Remote(object):
    def __init__(self, token,client=None,ip=None):
        self.token = token
        self.ip = ip
        self.client = client

        if self.ip != None:
            self.client = WebOSClient(self.ip)
            self.client.connect()
        else:
            self.client = WebOSClient.discover()[0]
            self.client.connect()
        
        for status in self.client.register(self.token):
            if status == WebOSClient.PROMPTED:
                print("Please accept the connection to TV !")
            elif status == WebOSClient.REGISTERED:
                print("Registration successful")

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
