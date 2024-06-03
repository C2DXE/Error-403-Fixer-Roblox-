import os

appdata=os.getenv('LOCALAPPDATA')
os.system(f"cd {appdata}")
directory = "Roblox"
path = os.path.join(appdata, directory)
os.system(f"rmdir /s /q {path}")
