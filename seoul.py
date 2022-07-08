import os
import rpc
import time
from tkinter import *
from time import mktime
from samp_client.client import SampClient

seoulIP = '198.251.81.84'
seoulPORT = '7777'

with SampClient(address = seoulIP, port = seoulPORT) as client:
    sampClientInfo = client.get_server_info()

def discord_rpc(name, state, details, largeText, smallText):
    print(f"[{name}] connecting...")
    client_id = '995065191601541283'
    rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)

    time.sleep(5)
    start_time = mktime(time.localtime())
    print(f"[{name}] connection successful.")

    activity = {
            "state": state,  
            "details": details, 
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": smallText,  
                "small_image": "smallimage", 
                "large_text": largeText,  
                "large_image": "largeimage"
            }
    }
    rpc_obj.set_activity(activity)
    time.sleep(900)        
    

def GetIn():
    os.system(f'sampcmd.exe -c -h {seoulIP} -p {seoulPORT} -n {userName}')
    discord_rpc("Discord Rich Presence", f"Modo: {sampClientInfo.gamemode}", f"{sampClientInfo.players} jugadores.", f"Usuario: {userName}", "Version: 0.3.DL-R1")

userName = input("Ingresa tu usuario: ")
GetIn()