#In this file theres functions to create json files

import json 
import os 

networkNames = ["YOLOV8", "YOLOV11", "YOLO26"]
networkVersionName = ["N", "S", "M", "L", "X"]


def WriteOutputNetworkAndVersion(network, networkVersion) :
    key = networkNames[network - 1] + networkVersionName[networkVersion - 1]
    r = {key : {}}
    return r, key; 



