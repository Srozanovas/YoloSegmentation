from ultralytics import YOLO
import models as m
import YOLOLaunch as y
import sys

# Input to select model 1

if sys.prefix == sys.base_prefix:
    print("Virtual environment is not active. To activate launch startVirtual or createVirtual!")
    exit(1)

#Select network 
[model, network, networkVersion] = m.getModel()

#launch yolo network 
y.launchYolo(model, network, networkVersion)












