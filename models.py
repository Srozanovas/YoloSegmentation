from ultralytics import YOLO
import torch
import os


def selectionInput(array): 
    selection = 0
    while selection == 0: 
        selection = input("Select (1-9): \r\n")
        if selection.isdecimal(): 
            selection = int(selection)
            if selection > len(array): 
                print("Unavailable selection")
                selection = 0 
        else:
            print("Error: select number")
            selection = 0
    return selection

def getNetworks(): 
    return ["1. YOLOV8", "2. YOLOV11", "3. YOLOV26"]

def getVersions(network): 
    match network: # YOLO V8
        case 1: return ["1. V8 n", "2. V8 s", "3. V8 m", "4. V8 l", "5. V8 x"]
        case 2: return ["1. V11 n", "2. V11 s", "3. V11 m", "4. V11 l", "5. V11 x"]
        case 3: return ["1. V26 n", "2. V26 s", "3. V26 m", "4. V26 l", "5. V26 x"]

def getPath(network, networkVersion): 
    path = "Models"; 
    match network: 
        case 1: 
            path += "/YOLOV8/yolov8"
            match networkVersion:
                case 1: path += "n"
                case 2: path += "s"
                case 3: path += "m"
                case 4: path += "l"
                case 5: path += "x"
            path += "-seg.pt"
        case 2: 
            path += "/YOLOV11/yolo11"
            match networkVersion:
                case 1: path += "n"
                case 2: path += "s"
                case 3: path += "m"
                case 4: path += "l"
                case 5: path += "x"
            path += "-seg.pt"
  
        case 3: 
            path += "/YOLOV26/yolo26"
            match networkVersion:
                case 1: path += "n"
                case 2: path += "s"
                case 3: path += "m"
                case 4: path += "l"
                case 5: path += "x"
            path += "-seg.pt"
    return path

def getWindowName(network, networkVersion): 
    name = ""
    match network: 
        case 1: name += "YOLOV8"
        case 2: name += "YOLOV11"
        case 2: name += "YOLOV26"

    match networkVersion: 
        case 1: name += "N segmentation"
        case 2: name += "S segmentation"
        case 3: name += "M segmentation"
        case 4: name += "L segmentation"
        case 5: name += "X segmentation"
    return name

def getModel():
    allNetworks = getNetworks()
    network = 0
    print("\nAVAILABLE NETWORKS")
    for n in allNetworks: 
        print(n); 
    network = selectionInput(allNetworks)
   

    #Select size of network 
    networkVersion = 0
    allVersions = getVersions(network)
    print("\nAVAILABLE VERSIONS")
    for v in allVersions:
        print(v)

    networkVersion = selectionInput(allVersions)

    networkPath = getPath(network, networkVersion)
    model = YOLO(networkPath)

    return [model, network, networkVersion]

def getVideoSource(): 
    folder_path = "Input"
    videos = ["WebCam"]
    videosinFolder = os.listdir(folder_path)
    for v in videosinFolder: 
        videos.append(v)   

    for index, v  in enumerate(videos):
        print(f"{index + 1}. {v}")

    videoIdx = selectionInput(videos)

    if videoIdx == 1: 
        return "webCam"
    else:
        return "Input/video" + str(videoIdx - 1) + ".mp4"

def getDevices(): 
    devices = ["CPU"]
    if torch.cuda.is_available():
        devices.append(f"GPU ({torch.cuda.get_device_name(0)})") 
    return devices 

def getDeviceName(): 
      
    allDevices = getDevices()
   
    for index, d  in enumerate(allDevices):
        print(f"{index + 1}. {d}") 

    device = selectionInput(allDevices)

    if device == 0: 
        return "cpu"
    else :
        return "cuda"
  
