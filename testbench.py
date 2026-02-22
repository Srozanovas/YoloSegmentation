from unittest.mock import patch
import models as m 
import YOLOLaunch as y
import output as o
import json
import os
import csv



NETWORKS = 3
VERSIONS = 5
DEVICE = 2


def RunTestbench() :
    for network in range (1, NETWORKS + 1): 
        for version in range (1, VERSIONS + 1):
            for device in range (1, DEVICE + 1):
            
                with patch("builtins.input", side_effect=[str(network), str(version), "2", str(device)]):
                    [model, network, networkVersion, videoPath, deviceName] = m.getModel()

                outputPath = m.getOutputPaths(network, networkVersion, deviceName)

                y.launchYolo(model, network, networkVersion, videoPath, deviceName, outputPath)
               


def ConvertJsonToCSV (folder): 
    NETWORKS = ["YOLOV8", "YOLOV11", "YOLOV26"]
    jsonList = [f for f in os.listdir("Output/" + NETWORKS[folder]) if f.endswith(".json")]
    AllData = {}
    for file in jsonList: 
        with open("Output/" + NETWORKS[folder] + "/" + file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for key in data.keys(): 
                if not key in AllData.keys(): 
                    AllData[key] = {}
                if data[key]["device"] == "CPU":
                    AllData[key]["CPUData"] = {}
                    AllData[key]["CPUData"]["AVG fps"] = data[key]["AVG fps"]
                    AllData[key]["CPUData"]["frames"] = data[key]["frames"]
                else :
                    AllData[key]["GPUData"] = {}
                    AllData[key]["GPUData"]["AVG fps"] = data[key]["AVG fps"]
                    AllData[key]["GPUData"]["frames"] = data[key]["frames"]

    with open("Output/" + NETWORKS[folder] + "/" + NETWORKS[folder] + ".csv", "w", newline="", encoding="utf-8") as ff:
        writer = csv.writer(ff)
    
        #Network names
        netRow = []
        for networkKey in AllData.keys():
            netRow += [networkKey, "", "", ""]
        writer.writerow(netRow)

        #Device names 
        netRow = []
        for networkKey in AllData.keys():
            for deviceKey in AllData[networkKey].keys():
                netRow += [deviceKey, ""]
        writer.writerow(netRow)

        #Average FPS 
        netRow = []
        for networkKey in AllData.keys():
            for deviceKey in AllData[networkKey].keys():
                netRow += ["Avg FPS", AllData[networkKey][deviceKey]["AVG fps"]]
        writer.writerow(netRow)
        netRow = []
        for networkKey in AllData.keys():
            for deviceKey in AllData[networkKey].keys():
                netRow += ["Frame ID", "NoP"]
        writer.writerow(netRow)

        #Frame info
        
        firstNet = next(iter(AllData))
        firstDevice = next(iter(AllData[firstNet]))
        numFrames = len(AllData[firstNet][firstDevice]["frames"])
        fpsArray = [[] for _ in range(numFrames)]

        for idx in range (0, numFrames):
            for netIDX, networkKey in enumerate(AllData.keys()):
                for devIDX, deviceKey in enumerate(AllData[networkKey].keys()):
                    fpsArray[netIDX*2+devIDX].append(AllData[networkKey][deviceKey]["frames"][idx]["NoP"])
        

        for idx in range (0, numFrames):
            netRow = []
            for netIDX, networkKey in enumerate(AllData.keys()):
                for devIDX, deviceKey in enumerate(AllData[networkKey].keys()):
                    netRow.append(idx)
                    netRow.append(fpsArray[netIDX*2+devIDX][idx])
            writer.writerow(netRow)
            
        

        

        



    

#RunTestbench()
ConvertJsonToCSV(2)