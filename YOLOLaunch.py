import ultralytics
import time
import cv2
import models as m
from collections import deque




# Create resizable window for each frame




def launchYolo(model, network, networkVersion):

    #Atvaizdavimo langas
    windowName = m.getWindowName(network, networkVersion) 
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(windowName, 1080, 720)

    #Gauname video vieta ir CPU ar GPU naudosime 
    videoPath = m.getVideoSource()
    deviceName = m.getDeviceName()


    #FPS kintamieji 
    prev_time = 0
    N = 30
    dt_hist = deque(maxlen=N)
    prev = time.perf_counter()

    
    for r in model(0 if videoPath == "webCam" else videoPath, stream=True, device=deviceName, imgsz=480, vid_stride=1, classes = 0):
        frame = r.plot()  # nupiešia box'us + maskes ant kadro

        #FPS SKAICIAVIMAS
        now = time.perf_counter()
        dt = now - prev
        prev = now

        dt_hist.append(dt)
        avg_dt = sum(dt_hist) / len(dt_hist)
        avg_fps = 1.0 / avg_dt if avg_dt > 0 else 0.0

        current_time = time.time()
        fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
        prev_time = current_time

        cv2.putText(frame, f"FPS: {fps:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Average FPS: {avg_fps:.2f}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow(windowName, frame)
        # q - uždaryti
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.waitKey(0)        
    cv2.destroyAllWindows()