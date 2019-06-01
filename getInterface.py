import os

def getInterface():
    interfaceList = []
    try:
        for root,dirs,files in os.walk('sys/class/net'):
            for dir in dirs:
                if dir[:3] == 'enx' or dir[:3] == 'eth' or dir[:4] == 'wlan':
                    interfaceList.append(dir)
    except:
        interFaceList.append("None")
    return interFaceList
